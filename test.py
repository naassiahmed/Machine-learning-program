import speech_recognition as sr  
import pyttsx3
import smtplib
from gensim.summarization import summarize
from gensim.summarization import keywords
from googletrans import Translator 
from textblob import TextBlob
from textblob import Word
from textblob.wordnet import VERB
from textblob.classifiers import NaiveBayesClassifier
from textblob.sentiments import NaiveBayesAnalyzer
from nltk.corpus import wordnet
from nltk.corpus import wordnet as wn
from summarize import summarize
import pytesseract
from PIL import Image
import time
import face_recognition
import os
from time import sleep

def takePicture():
	os.system("Py -2 sendmail.py")

def CheckFace(pathNewFace):
	known_image = face_recognition.load_image_file("ahmed.jpg")
	unknown_image = face_recognition.load_image_file(pathNewFace)

	biden_encoding = face_recognition.face_encodings(known_image)[0]
	unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

	results = face_recognition.compare_faces([biden_encoding], unknown_encoding)
	print (results)
	return results


def ImageToText(pathImg):
	pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files (x86)/Tesseract-OCR/tesseract.exe"
	img = Image.open(pathImg, mode='r')
	return(pytesseract.image_to_string(img))

def getDefinition(txt):
	print(Word(txt).definitions)
	return Word(txt).definitions

def getSynonyms(txt):
	synonyms = []
	
 
	for syn in wordnet.synsets(txt):
	    for l in syn.lemmas():
	        synonyms.append(l.name())
	         
	print(set(synonyms))
	
	return set(synonyms)

def getAntonyms(txt):
	
	antonyms = []
 
	for syn in wordnet.synsets(txt):
		for l in syn.lemmas():
			if l.antonyms():
				antonyms.append(l.antonyms()[0].name())
	print(set(antonyms))
	return set(antonyms)

def SpellCorrector(txt):
	b = TextBlob("I have goood speling and atrificial itelligance!")
	print(txt.correct())

def getSentiment(sent):
	train = [('I love this sandwich.', 'pos'),('this is an amazing place!', 'pos'),('I feel very good about these beers.', 'pos'),('this is my best work.', 'pos'),("what an awesome view", 'pos'), ('I do not like this restaurant', 'neg'),('I am tired of this stuff.', 'neg'),("I can't deal with this", 'neg'),('he is my sworn enemy!', 'neg'),('my boss is horrible.', 'neg'),('I like my friend.', 'pos'),('I hate eating sandwich.', 'neg')]
	test = [('the beer was good.', 'pos'),('I do not enjoy my job', 'neg'),("I ain't feeling dandy today.", 'neg'),("I feel amazing!", 'pos'),('Gary is a friend of mine.', 'pos'), ("I can't believe I'm doing this.", 'neg')]

	cl = NaiveBayesClassifier(train)

	opinion = TextBlob(sent,analyzer=NaiveBayesAnalyzer())
	print(opinion.sentiment)
	blob = TextBlob(sent, classifier=cl)
	print(blob.classify())
	print(cl.accuracy(test))
	
	
def detectLanguage(txtL):
	translator = Translator()
	detected = translator.detect(txtL)
	print(" Source Language:" + str(detected))


def translate(Lsrc,Ldest,txtL):
	translator = Translator()
	translated = translator.translate(txtL, src=Lsrc, dest=Ldest)

	print(" Source Language:" + translated.src)
	# Output: Source Language: ko

	print(" Translated string:" + translated.text) 
	# Output: Translated string

	print(" Pronunciation:", translated.pronunciation)
	return translated.text
	

def Summary(text):
	print ('Input text:')
	print (text)
	print ('Summary:')
	print (summarize(text,ratio=0.5))
	print ('Keywords:')
	print (keywords(text,ratio=0.5))
def ToSay(toSay):
	engine = pyttsx3.init()
	voices = engine.getProperty('voices')
	engine.setProperty('voice', "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0")
	rate = engine.getProperty('rate')
	engine.setProperty('rate', rate-70)
	engine.say(toSay)
	engine.runAndWait()
	engine.stop()
def ReportToMe(toSay):
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login("testpythontest2018@gmail.com", "ahmedahmedahmed")
	msg = toSay
	server.sendmail("testpythontest2018@gmail.com", "naas.si.ahmed@gmail.com", msg)
	server.quit()

def listenToMe():
	r = sr.Recognizer()                                                                                   
	r.dynamic_energy_threshold = False
	with sr.Microphone() as source:
		r.adjust_for_ambient_noise(source)                                                                       
		print("Speak:")                                                                                   
		audio = r.listen(source,timeout=3)   

	try:
	
		print("You said " + r.recognize_google(audio))
		return r.recognize_google(audio)
		#ToSay(r.recognize_google(audio))
		#ReportToMe(r.recognize_google(audio))
		#ReportToMe(Summary(r.recognize_google(audio)))
		#ReportToMe(translate('en','fr',r.recognize_google(audio)))
	except sr.UnknownValueError:
	    print("Could not understand audio")
	except sr.RequestError as e:
	    print("Could not request results; {0}".format(e))                                                                     


#dog = wn.synsets('program')
#print(dog)
#ToSay(getSynonyms('tea'));
#getDefinition('report')

#text="Artificial intelligence is among the most important technologies that will improve the daily lives of human-beings and promote further economic activities with potential revenues. Recently, there have been attempts towards developing a distributed intelligence, referred to as a global brain with a high-level of intelligence, that will, among others, optimize mobile services and their respective delivery networks. The global brain is defined as an architecture composed of different artificial intelligence entities that form a distributed intelligence. The architecture is inspired by the human nervous system whereby several neurons are connected.In this vein, this paper models the global brain architecture and the communications among its components based on multi-agent system technology and graph theory. The paper also targets two possible scenarios for the communications, proposing an optimized communication algorithm. The experiments, using JADE and JASON, showed a better performance of the global brain based on the optimized communication mechanism in terms of network complexity, network load and the number of exchanged messages. Furthermore, the paper discusses several emerging technologies that will support the development of the global brain future tasks such as voice recognition, image processing, natural language processing, big data processing and several machine learning functionalities."

#Summary(text)
#print(summarize(text, sentence_count=1, language='english'))

#ImageToText('C:/Users/SiAhmed/Documents/IoT and AI/neural/one class and normal class/ImageOpenC.png')

#CheckFace("atakor.png")

#os.system("Py -3 sendmail.py")
print('App started')

while (True):
	yourvar = input()
	if (yourvar=='initialize()'):
		print('Initialization completed !')
		ToSay('Initialization completed !')
	if (yourvar=='sayopeartion()'):
		ToSay('Please write down your desired speech')
		yourvar1 = input()
		ToSay(yourvar1)
	if (yourvar=='defineWord()'):
		ToSay('Please spell the word you want to define')
		valDef=listenToMe()
		ToSay(getDefinition(valDef))
	if (yourvar=='authenticate()'):
		ToSay('authentication process is just started')
		takePicture()
		sleep(6)
		ToSay('authentication completed !')
		checkFace=str(CheckFace("atakor.png")[0])
		if(str(checkFace)=="True"):
			print('-----------')
			print(CheckFace("atakor.png")[0])
			ToSay('Hello Mr. Ahmed, all rights are granted, welcome back. ')
			ToSay('How can I serve you?')
		else:
			ToSay('Failed to recognize you, system shutdown')
	if (yourvar=='getSynonyms'):
		ToSay('Please spell the word')
		txtsat=listenToMe()
		ToSay(getSynonyms(txtsat))
	

#checkFace=str(CheckFace("atakor.png")[0])
#if(str(checkFace)=="True"):
#	print('hola')
#for i in range(len(CheckFace("atakor.png"))):
#abc=CheckFace("atakor.png")[0]




#if(abc=="[True]"):
#	print('ok')