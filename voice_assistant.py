import webbrowser
import pyttsx3
import speech_recognition as sr 
r = sr.Recognizer()
engine = pyttsx3.init()

l = ["goodbye", "bye" , "bro stop", "stop playing", "take rest"]

websites = {
     "youtube" : "https://www.youtube.com/",
     "instagram" : "https://www.instagram.com/",
     "reddit" : "https://www.reddit.com/",
     "github" : "https://github.com/",
     "The souled store" : "https://www.thesouledstore.com/"}

songs = {
    "backdoor": "https://youtu.be/PzaAAGj4RC0?si=mB-BB02SbLao4cYE",
    "luther": "https://youtu.be/XVveECQmiAk?si=NmYxkoh4NbsR-Y6a",
    "kidhar": "https://youtu.be/PbN5elf37RY?si=L_S0xIvcr7Gl0dEI",
    "highest in the room": "https://youtu.be/OWl9p3oFKgg?si=nUDjSlipCOMVxCWY",
    "sau saal phle" : "https://youtu.be/sx6FTutCNaI?si=ZPny-BKAeuN9NcXJ",
    "long time" : "https://youtu.be/tkPoOvVnbRk?si=2ZIGXOY2p076aeXU",
    "i wanna be yours" : "https://youtu.be/IdAjA-cev2w?si=fR0WtYews-HeI4_m"}


while True:

    with sr.Microphone() as source:
        engine.say("start speaking")
        engine.runAndWait()
        print("Listening...")
        r.adjust_for_ambient_noise(source) 
        audio = r.listen(source)
    try:    
         command = r.recognize_google(audio)
         
    except:
         engine.say("Recongnition failed!!")
         engine.runAndWait()
         continue
    
    if command.lower() in l:
         engine.say("Have good day sir")
         engine.runAndWait()
         break

    elif command.lower() in websites:
         print("Opening....")
         a = websites.get(command.lower())
         webbrowser.open(str(a))
         continue
    
    elif command.lower() in songs:
         engine.say("enjoy the song")
         engine.runAndWait()
         b = songs.get(command.lower())
         webbrowser.open(str(b))
         continue

    else:
         engine.say("Not found Error")
         engine.runAndWait()
         engine.say("Speak again")
         engine.runAndWait()
         continue

    
 
    

