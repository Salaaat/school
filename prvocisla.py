import math

def vypisPrvocisla():

    min = input("Napiš dolní hranici>")
    while min.isdigit() == False:
        print("Zadej celé číslo!")
        min = input("Napiš dolní hranici>")
    min = math.ceil(float(min))

    max = input("Napiš horní hranici>")
    while max.isdigit() == False:
        print("Zadej číslo!")
        max = input("Napiš horní hranici>")
    max = math.ceil(float(max))
    
    if (min < 2 and max >= 2):
        min = 2
        
    prvocisla = []
    for i in range(min,max):
        prvocislo = True
        for x in range(2,i):
            if i % x == 0:
                prvocislo = False
        if i == 2:
            prvocislo = True
        if prvocislo:
            prvocisla.append(i)
    
    print(prvocisla)

vypisPrvocisla()
