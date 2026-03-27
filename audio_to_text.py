import speech_recognition as sr
import warnings
import whisper
import ffmpeg
import os

if not os.path.exists("input.wav"):
    print("Error: input file not found")
    exit()



#Initialize recognizer
recognizer = sr.Recognizer()
#warnings.filterwarnings("ignore",category=FutureWarning)   #uncomment this line if too unnecessary Warnings

input_path = r"input.wav"
if not os.path.exists("input.wav"):
    print("Error: input file not found")
    exit()
      
# Convert to 16kHz mono (better for speech recognition)
ffmpeg.input(input_path)\
      .output("processed.wav", ar=16000, ac=1)\
      .overwrite_output()\
      .run(quiet=True)

# Load the audio file
with sr.AudioFile("processed.wav") as source:
    print("Processing audio...")
    audio_data = recognizer.record(source)
try:
    text = recognizer.recognize_google(audio_data)
    print("Recognized Text:", text)
except sr.UnknownValueError:
    print("Speech Recognition could not understand the audio")
except sr.RequestError:
    print("Could not request results from Google API")



# Load the Whisper model (use "tiny", "base", "small", "medium", or "large")
model = whisper.load_model("medium")  # "base" is fast, "large" is most accurate






