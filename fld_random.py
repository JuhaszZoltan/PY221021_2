import random

for x in range(10):
    f31 = random.randint(100, 999)
    print(f'{f31}', end=' ')
print('\n----------------')

for x in range(10):
    f32 = random.random() * 25
    print(f'{round(f32, 1)}', end=' ')
print('\n----------------')

for x in range(10):
    f32_b = random.randint(0, 250) / 10
    print(f'{f32_b}', end=' ')
print('\n----------------')

for x in range(10):
    f33 = random.randint(150, 250) / 10
    print(f'{f33}', end=' ')
print('\n----------------')

for x in range(10):
    f34 = random.randrange(0, 100, 2)
    print(f'{f34}', end=' ')
print('\n----------------')

for x in range(10):
    f34b = random.randint(0, 49) * 2
    print(f'{f34b}', end=' ')
print('\n----------------')

for x in range(10):
    f35 = random.randint(20, 40) * 5 
    print(f'{f35}', end=' ')
print('\n----------------')