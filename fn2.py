# -*- coding: utf-8 -*-

from nltk.text import ConcordanceIndex
def phrasesContenant_bkp(corpus, mots):
	"""
	corpus: corpus tokenisé en phrases (liste de chaines)
	mots: liste de Synset
	retourne: la liste de toutes les phrases du corpus contenant ces synsets
	"""
	print("début phrasesContenant()")
	phrasesContenant = []
	index = ConcordanceIndex(corpus)
	
	#Pour chaque mot
	for mot in mots:
		positions = index.offsets(mot)
		print("positions:", positions)
		for position in positions:
			phrasesContenant.append(corpus[position])
	
	print("nb tokens:",len(phrasesContenant))
#	print("tokens:",phrasesContenant)
	print("fin phrasesContenant()")
	return phrasesContenant

import nltk
from nltk import word_tokenize
def phrasesContenant(phrases, mots):
	bonnesPhrases={}
	tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
	for phrase in phrases:
		phraseTokenisee = word_tokenize(phrase)
		for mot in mots:
			if mot in phraseTokenisee:
				try:
					bonnesPhrases[mot].append(phraseTokenisee)
				except:
					bonnesPhrases[mot]=[]
					bonnesPhrases[mot].append(phraseTokenisee)
	return bonnesPhrases
