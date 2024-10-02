## Features
- Download Instagram Reels from a provided URL.
- Convert video to audio for transcription.
- Generate transcripts with speaker identification and timestamps using **AssemblyAI**.
- View and export the transcript.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-repo-name/transcribe-reels.git
   cd transcribe-reels
   ```

2. **Install the required dependencies:**
   Ensure you have `pip` installed and run:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set your AssemblyAI API key:**
   Create an account at [AssemblyAI](https://www.assemblyai.com) and generate an API key. Set the API key in your project:
   ```python
   import assemblyai as aai
   aai.settings.api_key = "your-api-key-here"
   ```

4. **Run the app:**
   To start the app, run the following command:
   ```bash
   streamlit run transcribe.py
   ```

## How It Works

1. **Download Reels**: Provide an Instagram Reel URL, and the app downloads the video.
2. **Audio Conversion**: The video is converted into audio using **moviepy**.
3. **Transcription**: The audio is sent to AssemblyAI for transcription, including speaker identification.
4. **View Transcripts**: The transcription is displayed in the app with options to view speaker-specific dialogue.

## Requirements

- **Python 3.7+**
- **Streamlit**
- **Instaloader**
- **MoviePy**
- **AssemblyAI SDK**

For detailed dependencies, see the [requirements.txt](requirements.txt).

## Looking for Collaborators

I'm currently looking for **collaborators** to help with improving the **frontend** of this project. If you're skilled in **frontend development** and interested in working on this project, feel free to reach out!

## Contributing

Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a pull request.
