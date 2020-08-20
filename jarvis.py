import os
import pyttsx3

speaker = pyttsx3.init() 
speaker.setProperty('rate', 200) 
speaker.setProperty('volume', 3) 

voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0"
speaker.setProperty('voice', voice_id) 

print("")
print("\t||||||||||      |||       ||||||    ||         ||  ||  ||||||||")
print("\t    ||         || ||      ||   \|    ||       ||   ||  ||      ")
print("\t    ||        ||   ||     ||   /|     ||     ||    ||  ||____")
print("\t    ||       |||||||||    ||||||       ||   ||     ||        ||")
print("\t|\  /|      ||       ||   ||   ||       || ||	   ||        ||")
print("\t||_||      ||         ||  ||   ||        |||	   ||  ||||||||")

pyttsx3.speak("Hey Tony...! My name is Jarvis. I am your personal assistant.")
prog = ['chrome.lnk', 'edge.lnk', 'calendar.lnk', 'notepad', 'calc.exe', 'gmail.lnk', 'whatsapp.lnk']
ask = "What can I do for you?"
other = "What else can I do for you?"

while True:
        
	print("\nJarvis: ",ask)
	pyttsx3.speak(ask)
	ip = input("Type here: ").lower()
	
	if ' not ' in ip or 'do not' in ip or 'dont' in ip or "don't" in ip:
		print("\nJarvis: Okay!")
		pyttsx3.speak("Okay!")
		continue
		ask = other
	
	elif 'chrome' in ip:
		pyttsx3.speak("Opening chrome browser")
		os.system(prog[0])
		ask = other
	
	elif 'edge' in ip:
		pyttsx3.speak("Opening edge browser")
		os.system(prog[1])
		ask = other

	elif 'browser' in ip or (('browse' in ip or 'surf' in ip) and ('web' in ip or 'internet' in ip or 'net' in ip)):
		pyttsx3.speak("There are two browsers. Which one should I open? Chrome or edge?")
		print("Jarvis: Edge or Chrome?")
		browser = input("\n").lower()

		if 'better' in browser:
                        print("Yes! It definitely is.")        

		if 'edge' in browser:
			pyttsx3.speak("Opening edge browser")
			os.system(prog[1])			
			ask = other
		
		elif 'chrome' in browser:
			pyttsx3.speak("Opening chrome browser")
			os.system(prog[0])
			ask = other

		else: 			
			pyttsx3.speak("Sorry, I don't support this browser")
			ask = other
	
	elif 'schedule' in ip or 'calendar' in ip:
		pyttsx3.speak("Opening your calendar")
		os.system(prog[2])
		ask = other
	
	elif 'calculations' in ip or 'calculator' in ip or 'calculation' in ip:
		pyttsx3.speak("Opening calculator")
		os.system(prog[4])
		ask = other

	elif 'text editor' in ip or 'notepad' in ip or 'note' in ip:
		pyttsx3.speak("Opening notepad")
		os.system(prog[3])
		ask = other

	elif 'mail' in ip or 'email' in ip or 'gmail' in ip or 'e-mail' in ip or 'inbox' in ip:
		pyttsx3.speak("Opening Gmail")
		os.system(prog[5])
		ask = other

	elif 'message' in ip or 'call' in ip or 'whatsapp' in ip:
		pyttsx3.speak("Opening Whatsapp")
		os.system(prog[6])
		ask = other
		
	elif 'help' in ip:
		print("Hello! My name is Jarvis. I am your personal assistant. Here to make your life easier. Here are some commands that I understand:")
		pyttsx3.speak("Hello! My name is Jarvis. I am your personal assistan, here to make your life easier. Here are some commands that I understand:")		
		print("Keywords:\n\tBrowser - Chrome, Edge \n\tCalendar and E-mail \n\tCalculations and Note taking\n\tWhatsapp - Call, Message\n\thelp and exit ")
		ask = "So, what do you want me to do now?"
		
	elif 'exit' in ip or 'Thank you' in ip or 'will be all' in ip or 'quit' in ip:
		exyn = input("\nIf you want to exit then enter 1, else say anything else: ")
		if exyn == '1':
			pyttsx3.speak("Thank you for using Jarvis, Good Bye! Have a nice day!")	
			print("-----------------------------------------------------------------------------------")
			print("          Made by Shashwat Kothari, under the guidance of Vimal Daga Sir.")
			print("-----------------------------------------------------------------------------------")
			exit()
		else:
			continue
	
	else:
		print("\nSorry, I did not understand what you said. Run the help command to know what I can do. Try and repharase your command maybe I will understand.")
		pyttsx3.speak("Sorry, I did not understand what you said. Run the help command to know what I can do")
		ask = ""
