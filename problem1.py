import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Speak the text
engine.say("the story of an hour")

# Run the speech
engine.runAndWait()
