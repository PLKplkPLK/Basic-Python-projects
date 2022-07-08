from random import randint as rand


a = int(input("Zgaduj liczbę od: "))
b = int(input("do: "))

x = int(input("Ta liczba to: "))


zg = round((a+b)/2)
l=1
while zg != x:
    l+=1
    if zg > x:
        b = zg
    else:
        a = zg
    zg = rand(a,b)



print(f"Liczba to: {zg}, zajęło mi to {l} strzałów")