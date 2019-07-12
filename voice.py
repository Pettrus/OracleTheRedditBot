from gtts import gTTS

def speak(text, frame):
    tts = gTTS(text)
    tts.save("audios/" + str(frame) + ".mp3")