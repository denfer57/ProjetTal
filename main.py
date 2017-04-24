#!/bin/python3
# -*- coding: utf-8 -*-


from nltk import word_tokenize
import nltk
from fn1 import *
from fn2 import *
from fn3 import *
from fn4 import *
from fn5 import *

def getTexte():
	"""
	Retourne une chaine de caractère contenant l'intégralité du corpus.
	"""
	f=open('Corpus.txt')
	texte=f.read()
	return texte

def getSentenceTokens(texte):
	"""
	texte: chaine qu'on veut découper en phrases
	Retourne: liste de chaines (phrases du texte)
	"""
	tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
	return tokenizer.tokenize(texte)

def getTokensInSentences(phrases):
	"""
	Prend une liste de chaines représentant des phrases et divise ces phrases en tokens
	puis retourne le tout.
	
	Exemple :
	phrases: ["Ma phrase1 !", "Ma phrase 2."]
	return: [["Ma", "phrase1", "!"], ["Ma", "phrase", "2", "."]]
	"""
	phrasesTokenisees=[]
	for phrase in phrases:
		phrasesTokenisees.append(word_tokenize(phrase))
	return phrasesTokenisees
#phrasesTokenisees = getTokensInSentences(phrases)

#Pour tokenizer une chaine en mots :
#tokens = word_tokenize(texte)

texte=getTexte()
phrases = getSentenceTokens(texte)

motsCherches=synKill()
bonnesPhrases = phrasesContenant(phrases, motsCherches)
for phrase in bonnesPhrases:
	print(getSubject(phrase),"a tué à la date",getDate(phrase),"dans le lieu",getPlace(phrase))
#print(bonnesPhrases[motsCherches[0]][:4])
