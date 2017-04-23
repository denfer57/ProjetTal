#!/bin/python3
# -*- coding: utf-8 -*-

#On importe le corpus
#from nltk.corpus import PlaintextCorpusReader
#wordlists = PlaintextCorpusReader('../../', 'Corpus.txt')

#corpus = wordlists.words('Corpus.txt')

#Rechercher dans text1 :
#res = corpus.concordance("murderer")
#import nltk, re, pprint
from nltk import word_tokenize
import nltk

def getTexte():
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

#Recherche des synonymes
from nltk.corpus import wordnet as wn
def getSynonyms(word):
	list=[]
	for e in wn.synsets(word):
		list+=e.lemma_names()
	return list

#print(getSynonyms('murderer'))
#print(type(corpus)))

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

from fn2 import *

#corpus = nltk.Text(word_tokenize())
texte=getTexte()
phrases = getSentenceTokens(texte)


#tokens = word_tokenize(texte)
print("corpus monté")

motsCherches=['murderer']
bonnesPhrases = phrasesContenant(phrases, motsCherches)
print(bonnesPhrases[motsCherches[0]][:4])
