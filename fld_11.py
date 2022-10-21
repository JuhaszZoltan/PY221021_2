arlista:str = '''
=====ÁRLISTA=====
alma    350 Ft/Kg
körte  1200 Ft/Kg
szilva  500 Ft/Kg
'''
print(arlista)

vegosszeg:float = 0
kerdes:str = 'Jó napot kívánok! Szeretne valamit vásárolni? '
while input(kerdes) == 'igen':
    termek:str = input('Mit szeretne vásárolni? ')
    if termek not in {'alma', 'körte', 'szilva' }:
        print(f'Sajnálom, {termek} sajnos nincs :(')
    else:
        ar:int = 0
        if termek == 'alma': ar = 350
        elif termek == 'körte': ar = 1200
        elif termek == 'szilva': ar = 500
        mennyiseg:float = float(input(f'Hány Kg {termek}t szeretne? '))
        vegosszeg = vegosszeg + (ar * mennyiseg)
    kerdes = 'Szeretne még valamit vásárolni? '
print(f'Összesen {round(vegosszeg)} Ft-ot szeretnék kérni!\nViszont látásra!')