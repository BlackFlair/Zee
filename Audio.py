import speech_recognition as sr
import os
from gtts import gTTS
import datetime
import warnings
import calendar
import random
import wikipedia

warnings.filterwarnings('ignore')

def recordAudio():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print(">> Recording Audio ...")
        audio = r.listen(source)

    data = ''
    try:
        data = r.recognize_google(audio)
        print(data)
    except sr.UnknownValueError:
        print(">> Exception (sr.UnknownValueError): Google speech recognition could not understand the audio. ")
    except sr.RequestError as e:
        print(">> Exception (sr.RequestError): Request results from google speech recognition service error. ", e)

    return data

def assistantResponse(text):
    print(">> assistantResponse text : ", text)
    myobj = gTTS(text=text, lang='en', slow=False)

    myobj.save('Assistant_Response.mp3')

    os.system('start Assistant_Response.mp3')

def wakeWord(text):
    WAKE_WORDS = ['hey zee', 'okay zee', 'wake up zee', 'zee']

    text = text.lower()

    for phrase in WAKE_WORDS:
        if phrase in text:
            return True

    return False

def greeting(text):
    GREETING_INPUTS = ['hi zee', 'hey zee', 'hola zee', 'hello zee']
    GREETING_RESPONSE = 'hello sir.'

    for word in text.split():
        if word.lower() in GREETING_INPUTS:
            return GREETING_RESPONSE # random.choice(GREETING_RESPONSE) if GREETING_RESPONSE is a list of strings.

    return ''

def getTargetWord(text):
    wordList = text.lower().split()
    searchText = ''

    if 'web' in wordList and 'search' in wordList and wordList.index('search') == wordList.index('web')+1:
        index = wordList.index('search')

        if wordList[index+1] == 'for':
            index += 1

        for i in range(0, len(wordList)):
            searchText = searchText + " " + wordList[1+index+i]

        print(">> Word For Web Search : ", searchText)

    return searchText

while True:
    text = recordAudio()
    response = ''

    if wakeWord(text) == True:
        print(">> WAKE WORD Recognised ...")

        response = response + greeting(text)

    if 'web search' in text:
        searchText = getTargetWord(text)

        wiki = wikipedia.summary(searchText, sentences=3)

        response = response + " " + wiki

    assistantResponse(response)