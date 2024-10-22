import random
import string

noms = [''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(3,10))) for a in range(10)]
prenoms = [''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(3,10))) for a in range(10)]
age = [random.randint(16,30) for _ in range(10)]

tup = [(a,b,c) for a,b,c in zip(noms,prenoms,age)]

for t in tup:
    print(f"Le nom est {t[0]}, le prenome est {t[1]} et l'age est {t[2]}")