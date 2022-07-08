from random import choice as rch

def win(p, c):
    return (p == 'k' and c == 'n') or (p == 'p' and c == 'k') \
        or (p == 'n' and c == 'p')

d = {'k':'kamień', 'p':'papier', 'n':'nożyce'}


u = input("Co dajesz? Kamień 'k', papier 'p', nożyce 'n': ")
k = rch(['k','p','n'])


if u == k:
    print(f"Remis. Komputer i ty daliście {d[u]}")

elif win(u,k):
    print(f'Wygrałeś. Ty: {d[u]}, komputer: {d[k]}')

else:
    print(f'Przegrałeś. Ty: {d[u]}, komputer {d[k]}')