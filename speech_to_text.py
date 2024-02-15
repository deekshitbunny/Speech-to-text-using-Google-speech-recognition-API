import speech_recognition as sr
r = sr.Recognizer()
def listen_and_convert():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        print("Listening...")
        while True:  
            try:
                audio = r.listen(source, timeout=5) 
                print("Recognizing...")
                text = r.recognize_google(audio) 
                print("You said: {}".format(text))
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))
            except KeyboardInterrupt:
                print("\nExiting...")
                break  
# Exit the loop when CTRL+C is pressed
if __name__ == "__main__":
    listen_and_convert()