import random
import string
from pprint import pprint


cles = [''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(3,10))) for a in range(10)]
valeurs = [random.randint(1,1000) for a in range(10)]


dict_ini = {a:b for a,b in zip(cles,valeurs)}
pprint(dict_ini)
print("-"*30)

dict_new = {b:a for a,b in dict_ini.items()}
pprint(dict_new)