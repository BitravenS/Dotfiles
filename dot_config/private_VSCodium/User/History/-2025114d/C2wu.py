def findAll(s, f):
    res = []
    i = s.index(f)
    while i!=-1:
        res.append(i)
        i = s.rfind(f,i+1)
    return res

string = input("Donnez la chaine de referance: ").upper()
snippet = input("Donnez la sous chaine: ").upper()

print(findAll(string, snippet))