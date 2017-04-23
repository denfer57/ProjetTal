#retourne la date associée au verbe dans la phrase donnée.
import re
def getDate(sentence):
        regex = (January|February|March|April|May|June|July|August|September|October|November|December)[ ]([1-9]*|0[1-9])[,][ ]([0-9]{4})
