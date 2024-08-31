import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit

# Initialize the recognizer and text-to-speech engine
hear = sr.Recognizer()
speech = pyttsx3.init()

def speak(text):
    speech.say(text)
    speech.runAndWait()

def female():
    # Set the voice property to female
    speech.setProperty('voice', 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN-US_ZIRA_11.0')

def query():
    with sr.Microphone() as source:
        speak("Hello I'm your voice assistant. Please tell me what can I do for you?")
        
        while True:
            try:
                hear.adjust_for_ambient_noise(source)
                audio = hear.listen(source)
                query = hear.recognize_google(audio)
                print(f" {query}")

                if "hello" in query:
                    speak("Hello! How can I assist you today?")

                elif "how are you" in query:
                     speak("I'm doing well, thank you! How about you?")
                elif "your name" in query:
                    speak("I am your voice assistant Noa.")

                elif "play" in query.lower():
                    song_title = query.lower().replace("play", "").strip()
                    if song_title:
                        pywhatkit.playonyt(song_title)
                        speak(f"\nPlaying '{song_title}' on YouTube")
                    else:
                        speak("Please specify what you want to play.")
                
                elif "search" in query.lower() or "find" in query.lower():
                    search_query = query.lower().replace("search", "").replace("find", "").strip()
                    pywhatkit.search(search_query)
                    speech.say(f"Searching for {search_query}")
                    speech.runAndWait()

                elif "time" in query.lower() and "date" in query.lower():
                    datetime_query = query.lower().replace("date", "").replace("time", "").strip()
                    datetime_query = datetime.datetime.now().strftime("%I:%M %p, %B %d, %Y")
                    print(datetime_query)
                    speech.say(f"Today's date and time is {datetime_query}")
                    speech.runAndWait()

                elif "time" in query.lower():
                    time = datetime.datetime.now().strftime('%I:%M %p')
                    print(time)
                    speech.say(f"The time is {time}")
                    speech.runAndWait()

                elif "date" in query.lower():
                    date = datetime.datetime.now().strftime("%B %d, %Y")
                    print(date)
                    speech.say(f"Today's date is {date}")
                    speech.runAndWait()

                elif "stop listening" in query.lower() or "thank you, Alexa" in query.lower():
                    speak("Thank you")
                    break

            except sr.UnknownValueError:
                print("Listening....")
            except sr.RequestError as e:
                speak(f"Could not request results from Google; {e}")
                break

# Set the voice to female
female()

# Start the query function
query()
