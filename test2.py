import spacy
import pickle as pk
nlp  = spacy.load("en_core_web_sm")
results = ["a"]

with open("zz.pk", "wb") as f:
    pk.dump(results, f)