#retourne le lieu associé au verbe dans la phrase donnée.
from nltk.tag import pos_tag

def getPlace(sentence):
        toks_with_place=[]
        doc = pos_tag(sentence.split())
        toks_with_place = [word for word,pos in doc if pos == 'NNP']
        return toks_with_place

print(getPlace('I shot an elephant in Miami'))

