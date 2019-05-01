import pyaudio
import speech_recognition as s
r=s.Recognizer()

with s.Microphone() as source:
    print("please say something")
    audio=r.listen(source)

    try:

        txt=r.recognize_google(audio)

        print(f'you said : {txt}')
        f = open("demofile.txt", "w")
        f.write(txt)
    except:
        print("i cant undersatand what you said")
