# -*- coding: utf-8 -*-

from nltk.text import ConcordanceIndex
def phrasesContenant_bkp(corpus, mots):
	"""
	:DEPRECATED utiliser phrasesContenant() à la place
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
	"""
	:param phrases corpus tokenisé en phrases (liste de chaines)
	:param mots Liste de Synset
	retourne: la liste de toutes les phrases du corpus contenant ces synsets
	"""
	bonnesPhrases=[]
	for phrase in phrases:
		phraseTokenisee = word_tokenize(phrase)
		for mot in mots:
			if mot in phraseTokenisee:
				#try:
				bonnesPhrases.append(phrase)
				#except:
					#bonnesPhrases[mot]=[]
					#bonnesPhrases[mot].append(phrase)
	return bonnesPhrases

#print(phrasesContenant(['I would like to be an hero.', 'I am the boss, right now.', 'Are you OK?', 'Follow me, I am the boss, I said!'], ['am', 'OK']))
