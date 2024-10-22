import random
import string


cles = [''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(3,10))) for a in range(10)]
valeurs = [random.randint(1,1000) for a in range(10)]


dict_ini = {a:b for a,b in zip([])}