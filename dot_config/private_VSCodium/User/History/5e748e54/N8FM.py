from pprint import pprint

def findAll(s, f):
    res = []
    i = s.index(f)
    while i!=-1:
        res.append(i)
        i = s.rfind(f,i+1)
    return res

snip = input("Donnez votre chaine: ").lower()
words = set(snip.split(" "))

dicto = {a:len(findAll(snip,a)) for a in words}

pprint(dicto)