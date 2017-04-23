#retourne le lieu associé au verbe dans la phrase donnée.
from spacy.en import English
nlp = English()
def getPlace(sentence):
        toks_with_subject=[]
        doc = nlp(sentence)
        toks_with_subject = [tok for tok in doc if (tok.dep_ == "place") ]
        return toks_with_subject

print(getPlace('I shot an elephant in Miami'))

