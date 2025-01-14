"""Create video transcript with the Groq API.

Script adapted from the Groq API documentation:
https://console.groq.com/docs/speech-text
"""

from pathlib import Path

from groq import Groq

# Initialize the Groq client
client = Groq()

# Specify the path to the audio file
filename = Path(__file__).parent.absolute() / "audio_clean.mp3"

# Open the audio file
with open(filename, "rb") as audiofile:
    # Create a transcription of the audio file
    transcription = client.audio.transcriptions.create(
        file=(str(filename), audiofile.read()),
        model="whisper-large-v3",
        response_format="json",
        language="fr",
        temperature=0.0,
    )
    # Print the transcription text
    print(transcription.text)
