# CommentBot 🤖💬

**Proving the Dead Internet Theory by automating intelligent YouTube comments**

## Overview

**CommentBot** is a project designed to explore the "Dead Internet Theory" by creating a bot that can automatically comment on YouTube videos with relevant and meaningful statements. The bot combines several advanced technologies to achieve this, using YT-DLP for video/audio extraction, OpenAI's Whisper for transcription, and the LLaMA model for generating insightful comments from transcribed content.

With this project, we aim to show how AI can simulate intelligent interaction, blurring the lines between automated systems and human activity online.

---

## How It Works

1. **YouTube Video Download (YT-DLP)**  
   CommentBot starts by downloading YouTube videos (or audio) using [YT-DLP](https://github.com/yt-dlp/yt-dlp). YT-DLP extracts video/audio content and converts it into an MP3 format, suitable for transcription.

2. **Audio Transcription (OpenAI Whisper)**  
   After downloading the video/audio, [OpenAI Whisper](https://github.com/openai/whisper) transcribes the MP3 audio into text. Whisper is a state-of-the-art speech-to-text model that handles a wide variety of languages and complex audio environments.

3. **Generating Comments (LLaMA)**  
   The text transcription is then fed into [LLaMA](https://github.com/facebookresearch/llama), an advanced language model that generates contextually relevant YouTube comments based on the content of the video.

---

## Installation

### Prerequisites (Can be installed w/ pip in later steps)
- Python 3.8+
- `yt-dlp` (YouTube Downloader)
- `openai-whisper`
- LLaMA model setup
- ffmpeg (for audio processing)

### Clone the repository
```bash
git clone https://github.com/yourusername/CommentBot.git
cd CommentBot
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Run script
```bash
python3 bot.py
```

Then open comment.txt and see how it did.
