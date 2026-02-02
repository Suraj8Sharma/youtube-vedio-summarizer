# 📺 YouTube Video Summarizer

An intelligent tool that automatically extracts and summarizes YouTube video content using AI-powered natural language processing. This application helps users quickly understand video content without watching the entire video.

## 🌟 Features

- **Video Transcript Extraction**: Automatically fetches transcripts from YouTube videos
- **AI-Powered Summarization**: Generates concise summaries of video content
- **Chatbot Interface**: Interactive conversational interface for easy interaction
- **Batch Processing**: Support for multiple video summarization
- **Time-Saving**: Get the key insights from lengthy videos in seconds

## 📋 Table of Contents

- [Installation](#installation)
- [Requirements](#requirements)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [How It Works](#how-it-works)
- [Contributing](#contributing)
- [License](#license)

## 🚀 Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)
- Git

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/Suraj8Sharma/youtube-vedio-summarizer.git
   cd youtube-vedio-summarizer
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   # On Windows
   python -m venv venv
   venv\Scripts\activate

   # On macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install required dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables** (if required)
   Create a `.env` file in the root directory and add necessary API keys:
   ```
   # Add your API keys here if needed
   OPENAI_API_KEY=your_api_key_here
   # or other AI service keys
   ```

## 📦 Requirements

The project dependencies are listed in `requirements.txt`. Key libraries include:

- `youtube-transcript-api` - For extracting video transcripts
- `transformers` - For AI-based text summarization
- `flask` or `streamlit` - For web interface (depending on implementation)
- `nltk` or `spacy` - For natural language processing
- Other dependencies as specified in requirements.txt

To view all requirements:
```bash
cat requirements.txt
```

## 💻 Usage

### Basic Usage

1. **Start the application**
   ```bash
   # If using Jupyter Notebook
   jupyter notebook

   # If using Python script
   python main.py

   # If using Streamlit
   streamlit run app.py
   ```

2. **Enter YouTube URL**
   - Paste the YouTube video URL in the input field
   - Click "Summarize" or press Enter

3. **Get Summary**
   - Wait for the transcript extraction and summarization
   - View the generated summary

### Example

```python
# Example code snippet
from youtube_summarizer import VideoSummarizer

# Initialize the summarizer
summarizer = VideoSummarizer()

# Provide YouTube URL
url = "https://www.youtube.com/watch?v=VIDEO_ID"

# Get summary
summary = summarizer.summarize(url)
print(summary)
```

## 📁 Project Structure

```
youtube-vedio-summarizer/
│
├── CHATBOT/                    # Chatbot interface components
│   ├── [chatbot files]
│   └── ...
│
├── youtube_transcripts/        # Transcript extraction modules
│   ├── [transcript files]
│   └── ...
│
├── .gitignore                  # Git ignore file
├── requirements.txt            # Project dependencies
├── README.md                   # Project documentation (this file)
└── [other project files]
```

## 🔧 How It Works

1. **Video URL Input**: User provides a YouTube video URL
2. **Transcript Extraction**: The application uses `youtube-transcript-api` to fetch the video's transcript/captions
3. **Text Processing**: The transcript is cleaned and preprocessed
4. **Summarization**: AI models (like BART, T5, or GPT) generate a concise summary
5. **Output**: The summary is displayed to the user through the interface

### Supported Video Types

- Videos with automatic captions
- Videos with manual captions/subtitles
- Videos in multiple languages (depending on caption availability)

### Limitations

- Videos must have available transcripts/captions
- Live streams may not be supported
- Very long videos may take longer to process
- Some private or restricted videos cannot be accessed

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork the repository**
2. **Create a new branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Make your changes**
4. **Commit your changes**
   ```bash
   git commit -m "Add some feature"
   ```
5. **Push to the branch**
   ```bash
   git push origin feature/your-feature-name
   ```
6. **Open a Pull Request**

### Development Guidelines

- Follow PEP 8 style guidelines for Python code
- Add comments and documentation for new features
- Test your code before submitting
- Update README if you add new features

## 🐛 Troubleshooting

### Common Issues

**Issue**: "No transcript found"
- **Solution**: Ensure the video has captions/subtitles available

**Issue**: "API rate limit exceeded"
- **Solution**: Wait a few minutes before trying again or check API quota

**Issue**: "Module not found error"
- **Solution**: Make sure all dependencies are installed: `pip install -r requirements.txt`

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 👨‍💻 Author

**Suraj Sharma**
- GitHub: [@Suraj8Sharma](https://github.com/Suraj8Sharma)

## 🙏 Acknowledgments

- YouTube Transcript API developers
- Open-source AI/ML community
- Contributors and testers

## 📧 Contact

For questions, suggestions, or issues, please:
- Open an issue on GitHub
- Contact the repository owner

## 🔄 Updates and Roadmap

### Planned Features
- [ ] Support for multiple languages
- [ ] Downloadable summary as PDF/TXT
- [ ] Batch processing of multiple videos
- [ ] Custom summary length options
- [ ] Key timestamps extraction
- [ ] Video chapter-wise summarization

### Recent Updates
- Initial release with basic summarization
- Chatbot interface added
- Transcript extraction module implemented

---

⭐ If you find this project useful, please consider giving it a star on GitHub!

**Made with ❤️ by Suraj Sharma**
