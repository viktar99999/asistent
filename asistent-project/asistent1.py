import speech_recognition as sr
def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        task = r.recognize_google(audio, language="en-EN").lower()
        print("You speak " + task)
    except:
        task = command()
    return task

def makeSomething(task):
    print(task)
    if "сайт" in task:
        print("hello")
    elif "питон" in task:
        print("python<3")
    else:
        print("boring things")

while True:
    makeSomething(command())

