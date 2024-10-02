import instaloader
import streamlit as st
import moviepy.editor as mp
import os
import assemblyai as aai

# Set AssemblyAI API key
aai.settings.api_key = "AssemblyAI API key"
# Function to download Instagram Reel
def download_reel(url):
    try:
        loader = instaloader.Instaloader()
        loader.download_post(instaloader.Post.from_shortcode(loader.context, url.split('/')[-2]), target='reel')
        video_file = [f for f in os.listdir('reel') if f.endswith('.mp4')][0]
        return os.path.join('reel', video_file)
    except Exception as e:
        st.error(f"Error downloading reel: {e}")
        return None

# Function to convert video to audio
def convert_video_to_audio(video_file):
    clip = mp.VideoFileClip(video_file)
    clip.audio.write_audiofile("audio.wav")
    return "audio.wav"

# Function to transcribe audio using AssemblyAI SDK
def transcribe_audio(audio_file):
    transcriber = aai.Transcriber()

    # Transcribe the local audio file
    config = aai.TranscriptionConfig(speaker_labels=True)
    
    with open(audio_file, "rb") as f:
        transcript = transcriber.transcribe(f, config)

    if transcript.status == aai.TranscriptStatus.error:
        st.error(f"Transcription failed: {transcript.error}")
        return None

    return transcript

# Streamlit UI
st.title("Instagram Reels Transcription")

url = st.text_input("Enter Reel URL:")

if st.button("Transcribe Reel"):
    if url:
        st.write("Downloading Reel...")
        video_file = download_reel(url)
        
        if video_file:
            st.write("Converting video to audio...")
            audio_file = convert_video_to_audio(video_file)
            
            st.write("Transcribing audio...")
            transcript = transcribe_audio(audio_file)
            
            if transcript:
                st.write("Transcription Completed!")
                st.text_area("Transcript:", transcript.text)

                st.write("Speaker-wise transcription:")
                for utterance in transcript.utterances:
                    st.write(f"Speaker {utterance.speaker}: {utterance.text}")
            
            # Clean up files
            os.remove(video_file)
            os.remove(audio_file)
        else:
            st.error("Failed to download the reel.")
    else:
        st.error("Please enter a valid Reel URL.")
