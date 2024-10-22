import json

snip = input("Donnez votre phrase: ")

with open("en.json", "r") as j:
    stopwords = json.load(j)
j.close()


mots =[a for a in set(snip.split(" ").lower())&set(stopwords)]