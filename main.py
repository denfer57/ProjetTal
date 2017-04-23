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

def getTexte():
	f=open('../../Corpus.txt')
	texte=f.read()
	return texte

def getTokens(texte):
	print('début getTokens')
	tokens = word_tokenize(texte)
	print("fin getTokens")
	return tokens

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

from fn2 import *
import nltk
#corpus = nltk.Text(getTokens())
phrases = getSentenceTokens(getTexte())
print("corpus monté:",phrases)

bonnesPhrases = phrasesContenant(phrases, ['murderer'])
print(bonnesPhrases)