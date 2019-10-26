from pictures import *
import time as t
from random import *
import platform as plat
import os as o
def functionStart(secretWord=""):
	attemps = 1
	def functionEnterSecretWord():
		clear()
		print("1] JOUER EN SOLO")
		print("2] JOUER À PLUSIEURS")
		valueMod = int(input("\n"))
		if valueMod == 1:
			clear()
			try:
				with open("LOCALISATION/LIB/TEXT/mots.txt", "r") as file:
					carnet = []
					for ligne in file:
						carnet.append(ligne.strip(" \n"))
			except IOError:
				print("Ce programme nécéssite le fichier 'mots.txt'")
			else:
				word = choice(carnet)
				functionStart(word.lower())
		elif valueMod == 2:
			clear()
			word = input("\n\n[UTLISATEUR 1] => Veuillez entrer un mot à faire deviner : ")
			if len(word) < 5:
				print("\n\nVotre mot n'est pas assez long !")
			elif len(word) > 15:
				print("\n\nVotre mot est beaucoup trop long !")
			else:
				functionStart(word.lower())
		else:
			print("Une erreur est survenue...")

	def functionRestart():
		reply = input("\n\nVoulez vous rejouer ? [OUI / NON] : ")
		if reply == "Oui" or reply == "OUI" or reply == "oui" or reply == "yes" or reply == "Yes" or reply == "YES" or reply == "O" or reply == "o":
			clear()
			functionEnterSecretWord()
		elif reply == "Non" or reply == "noN" or reply == "non" or reply == "NON" or reply == "N" or reply == "n" or reply == "No" or reply == "no" or reply == "NO":
			clear()
			print("\n\nAu revoir, et peut être à bientôt")
			t.sleep(3)
		else:
			clear()
			print("\n\nUne erreur est survenue...")
			t.sleep(3)

	def functionDisplayIndication(indexLetter, secretWord):
		code = 5
		indication = ""
		for i in range(len(secretWord)):
			findLetter = False
			for index in indexLetter:
				if index == i and findLetter == False:
					indication += secretWord[i]
					findLetter = True
			if not findLetter:
				indication += "-"
		if indication == secretWord:
			return code
		else:
			return indication

	word = secretWord
	if word == "":
		functionEnterSecretWord()
	else:
		findLetter = []
		yourWord = ""
		indexLetter = []
		functionExecute(attemps)
		if indexLetter == []:
			indexLetter.append(16)
			if functionDisplayIndication(indexLetter, secretWord) == 5:
				yourWord = secretWord
				print("\n\n{}".format(secretWord))
			else:
				print("\n\n{}".format(functionDisplayIndication(indexLetter, secretWord)))
			del indexLetter[0]
		else:
			if functionDisplayIndication(indexLetter, secretWord) == 5:
				yourWord = secretWord
				print("\n\n{}".format(secretWord))
			else:
				print("\n\n{}".format(functionDisplayIndication(indexLetter, secretWord)))
		while yourWord != secretWord and attemps != 12:
			indexTwo = 0
			yourWord = input("\n\n[UTILISATEUR 2] => Veuillez essayer un mot ou une lettre : ")
			yourWord = yourWord.lower()
			if len(yourWord) == 1:
				if secretWord.find(yourWord) != -1:
					for k in range(0, len(secretWord), 1):
						if yourWord == secretWord[indexTwo]:
							indexLetter.append(indexTwo)
						indexTwo += 1
				else:
					attemps += 1
					varTempo = "".join(findLetter)
					print(varTempo)
					if varTempo.find(yourWord) == -1:
						findLetter.append(yourWord)
				if indexLetter == []:
					indexLetter.append(16)
					functionExecute(attemps)
					if functionDisplayIndication(indexLetter, secretWord) == 5:
						yourWord = secretWord
						print("\n\n{}".format(secretWord))
					else:
						print("\n\n{}".format(functionDisplayIndication(indexLetter, secretWord)))
					print("\n\nVos lettres fausses essayés sont {} !".format(findLetter))
					del indexLetter[0]
				else:
					functionExecute(attemps)
					if functionDisplayIndication(indexLetter, secretWord) == 5:
						yourWord = secretWord
						print("\n\n{}".format(secretWord))
					else:
						print("\n\n{}".format(functionDisplayIndication(indexLetter, secretWord)))
					if findLetter != []:
						print("\n\nVos lettres fausses essayés sont {} !".format(findLetter))
					
			else:
				if yourWord != secretWord:
					attemps += 1
				if indexLetter == []:
					indexLetter.append(16)
					functionExecute(attemps)
					if functionDisplayIndication(indexLetter, secretWord) == 5:
						yourWord = secretWord
						print("\n\n{}".format(secretWord))
					else:
						print("\n\n{}".format(functionDisplayIndication(indexLetter, secretWord)))
					if findLetter != []:
						print("\n\nVos lettres fausses essayés sont {} !".format(findLetter))
					del indexLetter[0]
				else:
					functionExecute(attemps)
					if functionDisplayIndication(indexLetter, secretWord) == 5:
						yourWord = secretWord
						print("\n\n{}".format(secretWord))
					else:
						print("\n\n{}".format(functionDisplayIndication(indexLetter, secretWord)))
					if findLetter != []:
						print("\n\nVos lettres fausses essayés sont {} !".format(findLetter))
		if attemps == 12:
			print("\n\nDésolé, vous avez perdu, le mot était {}".format(secretWord))
			functionRestart()
		elif yourWord == secretWord:
			if plat.system() == "Windows":
				o.system("color a")
			if (attemps-1) == 1:
				print("\n\nBravo, vous avez gagné et vous avez fait une erreur !!!".format())
				functionRestart()
			else:
				print("\n\nBravo, vous avez gagné et vous avez fait {} erreurs !!!".format(attemps-1))
				functionRestart()
functionStart()