#taking the necessary imports
from youtube_transcript_api import YouTubeTranscriptApi,TranscriptsDisabled
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint,HuggingFaceEmbeddings,HuggingFaceEndpointEmbeddings

from urllib.parse import urlparse, parse_qs
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel, RunnablePassthrough,RunnableLambda
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
from dotenv import load_dotenv
load_dotenv()
import os 
import shutil
#our vector_database
from langchain_chroma import Chroma

#DOCUMENT INGESTION:-THE YOUTUBE VIDEO TRANSCRIPT WE ARE LOADING HERE 


def get_transcript_from_url(video_url):
    
    try:
        # 1. Extract Video ID (Handles standard and short URLs)
        parsed_url = urlparse(video_url)
        if "youtu.be" in video_url:
            video_id = parsed_url.path[1:]
        else:
            video_id = parse_qs(parsed_url.query).get("v")[0]
           
        #we will try to get the youtube transcript form the youtube id by using the youtube video transcript

        fetched_transcript=YouTubeTranscriptApi().fetch(video_id,languages=["en"])
        # FetchedTranscript(snippets=[FetchedTranscriptSnippet(text='Enhancement of construction and', start=6.799, duration=4.96), FetchedTranscriptSnippet(text='infrastructure equipments, high-speed', start=8.96, duration=6.24), FetchedTranscriptSnippet(text='rail corridors as growth connectors,', start=11.759, duration=6.321), FetchedTranscriptSnippet(text='individual persons resident outside', start=15.2, duration=5.68), FetchedTranscriptSnippet(text='India will be permitted to invest in', start=18.08, duration=5.279), FetchedTranscriptSnippet(text='equity instruments, medical tourism': 2.0}
        #the above is the one which is expected ny the above
        transcript_list=fetched_transcript.to_raw_data()

        #the above step return a list so we will flattent that into a plain text
        transcript=" ".join([d["text"] for d in transcript_list])

        return transcript
    except TranscriptsDisabled:
        print("Transcripts are disabled for this")
        return None  #ADDED: return None when transcript fetch fails

def  summarize(transcript,question):
        #WE WILL BREAK OUR DOCUMENTS INTO CHUNKS SO WE WILL DO 
        splitter=RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
        )
       

        #BREAKING DOWN INTO CHUNKS
        chunks=splitter.split_text(transcript)
        embeddings = HuggingFaceEndpointEmbeddings(
        repo_id="sentence-transformers/all-MiniLM-L6-v2",
        task="feature-extraction"
    )
        #vector-store
        vector_store=Chroma(
        embedding_function=embeddings,
        collection_name="youtube_transcripts"
        )

        vector_store.add_texts(chunks)

        #SETTING UP OUR RETREIVER
        retriever=vector_store.as_retriever(search_type="similarity",search_kwargs={"k":4}) 
        prompt=PromptTemplate(
     template="""You are a helpful AI assistant that answers questions based on YouTube video transcripts.

Context from the video transcript:
{context}

User Question: {question}

Instructions:
- Answer the question directly and comprehensively based ONLY on the context provided
- Provide detailed explanations with at least 100-150 words when possible
- Use bullet points or numbered lists when appropriate for clarity
- Include specific examples, statistics, or quotes from the transcript when available
- If the context doesn't contain enough information to answer the question, say "I don't have enough information in this video transcript to answer that question."
- Keep your answer well-structured and informative
- Don't add information that's not in the context

Answer:""",
input_variables=["context","question"])
        llm=HuggingFaceEndpoint(
    repo_id = "mistralai/Mistral-7B-Instruct-v0.2",
    task="text-generation"
)
        #OUR MODEL BASICALLY FOR THE ANSWERING WITH THE CONTEXT
        model=ChatHuggingFace(llm=llm,temperature=0.2)
        parser=StrOutputParser()


        def format_text(text):
            #FIXED: Added check for page_content attribute to prevent AttributeError
            context_text=" ".join(doc.page_content if hasattr(doc, 'page_content') else str(doc) for doc in text)
            return context_text

        parallel_chain=RunnableParallel({
        "context":retriever|RunnableLambda(format_text),
        "question":RunnablePassthrough()
    })

        #MAKING CHAINS FOR THE PREDICTION PURPOSE 
        sequence_chain=prompt|model|parser
        final_chain=parallel_chain|sequence_chain

        result=final_chain.invoke(question)
        return result

#now its the time for the streamlit ui 
st.title("🎥 YouTube Video Q&A Assistant")  #CHANGED: Better heading with emoji
st.markdown("Ask questions about any YouTube video and get AI-powered answers!")  
video_url = st.text_input("Paste your YouTube Link here:", placeholder="https://www.youtube.com/watch?v=...")

if video_url:
    st.write(f"You entered: {video_url}")
question=st.text_input("Enter Your Question:")
#now making a submit button 
if(st.button("Submit")):
    with st.spinner("🔍 Fetching transcript and analyzing..."):
        transcript=get_transcript_from_url(video_url)

    
        #FIXED: Added error handling for when transcript is None 
        if not transcript:
            st.error("Could not fetch transcript. Transcripts may be disabled for this video.")
        else:
            result=summarize(transcript,question)

            if result:
                st.write(result)