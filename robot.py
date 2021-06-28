import speech_recognition
import pyttsx3
import gtts
import os
from datetime import date, datetime
robot_ear = speech_recognition.Recognizer()
robot_mouth = pyttsx3.init()
def robot_answer(robot_brain):
    print("Robot:" + robot_brain)
    robot_mouth.say(robot_brain)
    robot_mouth.runAndWait()
    return;
while True: 
    with speech_recognition.Microphone() as mic:
        print("Robot: I'm Listening")
        audio = robot_ear.listen(mic)    
    print("Robot:...") 
    try:
        you = robot_ear.recognize_google(audio)
        print("User: " + you)
    except:
        you = ""
    if you == "":
        robot_brain = "I can't hear you, try again"
        robot_answer(robot_brain)
    elif "hello" in you: 
        robot_brain = "Hello Python"
        robot_answer(robot_brain)
    elif "today" in you:
        today = date.today()
        robot_brain = today.strftime("%B %d,%Y")
        robot_answer(robot_brain) 
    elif "time" in you:
        now = datetime.today()
        robot_brain = now.strftime("%H : %M : %S")
        robot_answer(robot_brain)    
    elif "weather" in you:
        robot_brain= "I don't know, try again"
        robot_answer(robot_brain)        
    elif "bye" in you: 
        robot_brain = "Good Bye, see you again"
        robot_answer(robot_brain)
        break
    else:
        robot_brain = "I'm fine thank you and you"
        robot_answer(robot_brain)
        

