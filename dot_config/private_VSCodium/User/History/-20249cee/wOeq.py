from pprint import pprint

def words(s):
    dicty = {a:len(a) for a in s.split(" ")}
    return dicty

snip = input("Donnez votre phrase: ")
pprint(words(snip))