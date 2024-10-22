import json

snip = input("Donnez votre phrase: ")

with open("en.json", "r") as j:
    stopwords = json.load(j)
j.close()

stopwords = (a.lower() for a in stopwords)

mots =[a for a in set(snip.lower().split(" "))&set(stopwords)]
print(mots)