import speech_recognition as sr

recognizer = sr.Recognizer() # Initialize the recognizer
mic = sr.Microphone() # Use the default systems mic

# This function listens from the mic and puts what you say into a string.
def listen_command():
    with mic as source:
        recognizer.adjust_for_ambient_noise(source) # Adjust for ambient noise to improve recognition accuracy
        print("Listening...") # just to let you knbow its working

        audio = recognizer.listen(source) # function that listens from your mic

    try:
        text = recognizer.recognize_google(audio).lower() # Use Google's speech recognition to convert audio to text and convert it to lowercase for easier processing  
        print("Heard:", text)
        return text
    except:
        return ""

# Write a function that processes these command and makes the drone do things

# Write a loop that listens for commands and then processes them. You can use the "listen_command" function to get the command and then use an if statement to check what the command is and make the drone do something based on that.