#retourne qui est le sujet du verbe dans la phrase donnée.
from spacy.en import English
nlp = English()
def getSubject(sentence):
        toks_with_subject=[]
        doc = nlp(sentence)
        toks_with_subject = [tok for tok in doc if (tok.dep_ == "nsubj") ]
        return toks_with_subject

print(getSubject('I shot an elephant'))
