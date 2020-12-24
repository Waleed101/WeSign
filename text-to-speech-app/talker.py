import pyttsx3

# initialize engine
engine = pyttsx3.init()

# set properties
engine.setProperty('rate', 150) # speed percent
engine.setProperty('volume', 0.9) # Volume 0-1

# Text-to-speech function
def speak(s):
    engine.say(s)
    engine.runAndWait()
