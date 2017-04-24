# -*- coding: utf-8 -*-

import re, nltk
from nltk import word_tokenize
def getDate(phrase):
	"""
	:param phrase Phrase tokenisée (liste de chaines).
	retourne la date associée au verbe dans la phrase donnée.
	"""
	#regex = (January|February|March|April|May|June|July|August|September|October|November|December)[ ]([1-9]*|0[1-9])[,][ ]([0-9]{4})

	phraseTaggee=nltk.pos_tag(word_tokenize(phrase))
	phraseChunkee=nltk.ne_chunk(phraseTaggee)

	grammar = r"DATE: {<NNP><CD>}"
	parser=nltk.RegexpParser(grammar)

	phraseDatee=parser.parse(phraseChunkee)
			
	return [word for word in phraseDatee if isinstance(word, nltk.tree.Tree) and word.label()=='DATE']

#print(getDate("I left Paris in October 2010, two days before my death."))
