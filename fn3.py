#retourne qui est le sujet du verbe dans la phrase donnée.
from nltk.tag import pos_tag
from nltk import word_tokenize

def getSubject(sentence):
        toks_with_subject = []
        doc = pos_tag(word_tokenize(sentence))
        toks_with_subject = [word for word,pos in doc if pos == 'PRP']
        return toks_with_subject

#print(getSubject('I shot an elephant in Miami'))
