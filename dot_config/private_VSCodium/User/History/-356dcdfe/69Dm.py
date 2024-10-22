import json

snip = input("Donnez votre phrase: ")

with open("en.json", "r") as j:
    stopwords = json.load(j)
j.close()
print(stopwords)