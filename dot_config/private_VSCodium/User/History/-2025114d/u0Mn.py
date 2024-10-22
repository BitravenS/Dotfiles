def findAll(s, f):
    res = []
    i = s.index(f)
    print(i)
    while i!=-1:
        res.append(i)
        s = s[i+1]
        i=s.index(f)
        print(i)
    return res

string = input("Donnez la chaine de referance: ").upper()
snippet = input("Donnez la sous chaine: ").upper()

print(findAll(string, snippet))