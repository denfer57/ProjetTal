from nltk.stem.wordnet import wordnet as wn

def synKill():
    tab=[]
    for ss in wn.synset('kill.v.01').hyponyms():
        tab += ss.lemma_names()
    print(tab)

def listeCorpus(listeSynsets): #prend une liste de synsets et retourne la liste des phrases du corpus ayant ces synsets
    
    return listePhrases
