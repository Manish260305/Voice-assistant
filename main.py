print("✅ Starting assistant.py")  

import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import os
import sys
import pytz
import random

print("✅ Libraries loaded")  

engine = pyttsx3.init()
engine.setProperty('rate', 170)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) 

def talk(text):
    print("🎙️ MANISH:", text)
    engine.say(text)
    engine.runAndWait() 

def take_command():
    listener = sr.Recognizer()
    try:
        with sr.Microphone(device_index=0) as source: 
            print("🎧 Listening...")
            listener.adjust_for_ambient_noise(source)
            print("Mic adjusted, now listening...")
            voice = listener.listen(source, timeout=5, phrase_time_limit=5)

        command = listener.recognize_google(voice)
        command = command.lower()
        print("🗣️ You said:", command)
        return command

    except sr.WaitTimeoutError:
        talk("I didn’t hear anything. Please speak louder.")
        return ""
    except sr.UnknownValueError:
        talk("Sorry bro, I didn’t catch that.")
        return ""
    except sr.RequestError:
        talk("Network issue with Google service.")
        return ""
    except Exception as e:
        print("❌ Error:", e)
        talk("Something went wrong with the microphone.")
        return ""

def run_manish():
    print("🛠 run_manish() called")
    command = take_command()
    print("📥 Got command:", command)

    if "play" in command:
        song = command.replace("play", "").strip()
        talk("Playing on YouTube 🎶")
        pywhatkit.playonyt(song)

    elif "what's the time" in command:
        ist = pytz.timezone('Asia/Kolkata')
        time = datetime.datetime.now(ist).strftime('%I:%M %p')
        talk(f"The time in India is {time} 🕰")

    elif "who is manish codes" in command or "who is manish_codes" in command:
        info = (
            "Manish, known as manish_codes on Instagram, is a coding content creator. "
            "He teaches Python projects in Telugu and shares cool tech tutorials 💻"
        )
        talk(info)

    elif "who is" in command:
        person = command.replace("who is", "").strip()
        try:
            info = wikipedia.summary(person, sentences=1)
            talk(info)
        except:
            talk("Sorry, I couldn’t find information about that person.")

    elif "joke" in command:
        joke_type = random.choice(['text', 'custom'])

        if joke_type == 'text':
            joke = pyjokes.get_joke()
            talk(joke)
        else:
            jokes = [
                "Why don’t scientists trust atoms? Because they make up everything!",
                "Why did the developer go broke? Because he used up all his cache!",
                "I told my laptop it was running slow... it started jogging.",
                "Parallel lines have so much in common. It’s a shame they’ll never meet.",
                "Debugging: where you fix one bug and create five more. Welcome to coding!"
            ]
            talk(random.choice(jokes))

        sunil_search_url = "https://www.youtube.com/results?search_query=sunil+telugu+comedy+scenes"
        talk("Want more fun? Watch Sunil's comedy here 😂:")
        talk(sunil_search_url)

    elif "open chrome" in command:
        chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        if os.path.exists(chrome_path):
            talk("Opening Chrome 🚀")
            os.startfile(chrome_path)
        else:
            talk("Chrome path not found 😬")

    elif "open code" in command or "open vs code" in command:
        talk("Opening VS Code 💻")
        os.system("code")

    elif "exit" in command or "stop" in command:
        talk("Okay bro, see you later 👋")
        sys.exit()

    elif command != "":
        talk("I heard you, but I don’t understand that yet 😅")

talk("Yo! I'm MANISH – your personal voice assistant 💡")

while True:
    run_manish()
