import random

# [0, 1) -> float 
r1 = random.random()
print(r1)

# [a, b] -> a < b
r2 = random.randint(-30, 40)

# [start, stop) 'setp'esével ==> int
r3 = random.randrange(start=8, stop=21, step=3)