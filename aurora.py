import os
import webbrowser
import wikipedia
import datetime
import speech_recognition as sr
import  pyttsx3
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices)
engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning ")
    elif hour>=12 and hour<18:
        speak("good afternoon ")
    else :
        speak("good evening")

##def email(to,content):
    
    
def takecommand():
    # takes input from mic and returns a string
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening..........")
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("Recognizing.......")
            query = r.recognize_google(audio)
            print("user said:",query)
        except Exception as e:
##            print(e)
            print("say that again please....")
            return "None"
        return query

if __name__=="__main__":
     #speak("hamid is great")
     wishme()
     speak("my name is aurora how may i help you ")
     brave_path = '"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe" %s'
##     webbrowser.get(brave_path).open('google.com')
     while True:

         query= takecommand().lower()
         if 'wikipedia' in query:
             speak("searching wikipedia......")
             query = query.replace("wikipedia","")
             results = wikipedia.summary(query, sentences=2)
             speak("according to wikipedia ")
             print(results)
             speak(results)
         elif ' youtube'  in query:
##              webbrowser.get(brave_path).open('youtube.com')
             webbrowser.open('youtube.com')
         elif 'google' in query:
              webbrowser.open('google.com')
         elif 'play music' in query:
             m_dir='G:\\music'
             songs=os.listdir(m_dir)
             print(songs)
             os.startfile(os.path.join(m_dir,songs[0]))
         elif 'time' in query:
              strtime=datetime.datetime.now().strftime("%H:%M:%S")
              speak(f"the time is {strtime}")
         elif 'open brave' in query:
             bravepath="C:\Program Files\BraveSoftware\Brave-Browser\Application\\brave.exe"
             os.startfile(bravepath)
         elif 'shut down' or 'shutdown' in query:
##              spath="C:\Windows\system32\shutdown.exe"
##              os.startfile(spath)
                 os.system("shutdown /s /t 1")
                  
     '''    elif 'emailtohamid' in query:
             try:
                 speak("what should i say?")
                 content=takecommand()
                 email(to,content)
                 speak("email has been sent")
             except Exception as e:
                 print(e)
                 speak("sorry ; aurora has failed to send the e-mail")
                  '''
     
         





             
