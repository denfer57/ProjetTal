from nltk.stem.wordnet import wordnet as wn

def synKill():
    tab=['kill']
    for ss in wn.synset('kill.v.01').hyponyms():
        tab += ss.lemma_names()
    return tab

#print(synKill())
