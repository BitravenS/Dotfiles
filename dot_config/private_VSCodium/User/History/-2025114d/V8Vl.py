def findAll(s, f):
    res = []
    i = s.find(f)
    while i!=-1:
        res.append(i)
        i=s[:i+1].find(f)