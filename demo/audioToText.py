import speech_recognition as sr

def listen_and_transcribe():
    # Initialize the recognizer
    recognizer = sr.Recognizer()

    # Use the microphone as the source
    with sr.Microphone() as source:
        print("Adjusting for ambient noise... Please wait.")
        recognizer.adjust_for_ambient_noise(source)
        print("Listening...")
        
        # Listen for audio and record it
        audio_data = recognizer.listen(source)
        print("Recognizing...")
        
        try:
            # Recognize speech using Google Web Speech API
            text = recognizer.recognize_google(audio_data)
            print(f"Transcription: {text}")
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")

if __name__ == "__main__":
    listen_and_transcribe()