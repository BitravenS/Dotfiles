import random
import string
from pprint import pprint

noms = [''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(3,10))) for a in range(10)]
prenoms = [''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(3,10))) for a in range(10)]
note = [random.randint(8,20) for _ in range(10)]

dicto = {(a,b):c for a,b,c in zip(noms,prenoms,note)}
pprint(dicto)

i = set(input("Donnez le nom et prenom separe par une espace: ").split(" "))
print(dicto[i])