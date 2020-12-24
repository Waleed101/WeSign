from talker import speak
from wordParser import stringToWords

# returns speech form of user asl letter input
def stringToSpeech(s):
    sentence = stringToWords(s)
    speak(sentence)

# test
s = 'thisisthestringwithnospacesletusseeifitworksalsoheisstillawastemanhahalookslikeitworks'
stringToSpeech(s)