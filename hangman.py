from wyrazy import words as wyrazy
from random import choice as rch

def dobre_slowo(w):
    while True: #można też while '-' or ' ' in word: inne słowo
        s=rch(w)
        if s.isalpha():
            break
    return s

def wisielec():
    s = dobre_slowo(wyrazy)
    życia = len(s)
    print(f'(słowo to {s})')
    x = '_'*len(s)
    l = set(s)
    użyte = set()
    while życia > 0:
        if not '_' in x:
            print(f"Gratulacje, słowo to {s}")
            return
        print(f'Słowo do zgadnięcia: {x}, żyć: {życia}')
        print('Użyłeś już: ', ', '.join(użyte))
        lu = input("Zgadnij literę: ")
        użyte.add(lu)
        if lu in l:
            l.remove(lu)
            x = [c if c in użyte else '_' for c in s]
            x = ''.join(x)
        else:
            życia -= 1
        
    print("Przegrałeś")

wisielec()