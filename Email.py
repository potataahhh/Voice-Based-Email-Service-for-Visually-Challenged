import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage

listener = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()

def get_info():
    with sr.Microphone() as source:
        print('listening...')
        voice = listener.listen(source)
        try:
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()
        except:
           print("not working")

def send_email(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('ayush.aj.789@gmail.com', 'kuttakamina#1')
    email = EmailMessage()
    email['From'] = 'ayush.aj.789gmail.com'
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)


email_list = {
    'dad': 'rkc169@gmail.com',
    'myself': 'ayush.aj.789@gmail.com',
    'meena': 'meenalphartiyal17@gmail.com',
    'mridul': 'mridulrastogi100@gmail.com',
    'omy': 'omjasharma287@gmail.com'
}


def get_email_info():
    talk('To Whom you want to send email')
    name = get_info()
    receiver = email_list[name]
    print(receiver)
    talk(' What is the subject of your email? ')
    subject = get_info()
    talk(' Content of your email ')
    message = get_info()
    send_email(receiver, subject, message)
    talk(' Your email is sent')
    talk('Do you want to send more email?')
    send_more = get_info()
    if 'yes' in send_more:
        get_email_info()




get_email_info()
