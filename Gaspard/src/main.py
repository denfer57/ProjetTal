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
def getTokens():
	f=open('../../Corpus.txt')
	raw=f.read()
	tokens = word_tokenize(raw)
	return tokens
	

#Recherche des synonymes
from nltk.corpus import wordnet as wn
def getSynonyms(word):
	list=[]
	for e in wn.synsets(word):
		list+=e.lemma_names()
	return list

print(getSynonyms('murderer'))
#print(type(corpus)))