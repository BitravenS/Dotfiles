import random
import string

noms = [''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(3,10))) for a in range(10)]
prenoms = [''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(3,10))) for a in range(10)]
age = [random.randint(16,30) for _ in range(10)]