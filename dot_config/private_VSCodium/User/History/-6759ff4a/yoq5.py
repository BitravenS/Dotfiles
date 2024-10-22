import random
import string

noms = [''.join(random.choice(string.ascii_lowercase) for _ in range(10)) for a in range(10)]
print(noms)