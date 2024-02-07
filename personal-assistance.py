import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
listener = sr.Recognizer()
engine = pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()
def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening..")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
    except:
        pass
    return command
def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play','')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M %p')
        print(time)
        talk('Current time is' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry,I have a headache')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'are you single' in command:
        talk('I am in a relationship with siri')
    elif 'male' in command:
        talk('I am an male')
        print('I am a male')
    elif 'married' in command:
        talk('i will not tell my answer to singles')
    elif 'siri' in command:
        talk('dont talk about that idiot')
        print('dont talk about that idiot')
    elif 'movie' in command:
        talk('Thuppaki')
        print('Thuppaki')
    else:
        talk('Please say the command again')

run_alexa()
