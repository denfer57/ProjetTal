#retourne le lieu associé au verbe dans la phrase donnée.
from nltk.tag import pos_tag
from nltk import word_tokenize

def getPlace(sentence):
        toks_with_place=[]
        doc = pos_tag(word_tokenize(sentence))
        toks_with_place = [word for word,pos in doc if pos == 'NNP']
        return toks_with_place

#print(getPlace('I shot an elephant in Miami'))

