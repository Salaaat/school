import math

def zkontrolujCislo(x):
    try:
        float(x)
    except ValueError:
        return False

def zkontrolujNenuloveCislo(x):
    try:
        float(x)
        if float(x) != 0:
            return True
        else:
            return False
    except ValueError:
        return False

a = input("Zadej nenulový kvadratický člen>")
while zkontrolujNenuloveCislo(a) == False:
        print("Zadej nenulové číslo!")
        a = input("Zadej nenulový kvadratický člen>")
a = float(a)

b = input("Zadej lineární člen>")
while zkontrolujCislo(b) == False:
        print("Zadej číslo!")
        b = input("Zadej lineární člen>")
b = float(b)

c = input("Zadej konstantní člen>")
while zkontrolujCislo(c) == False:
        print("Zadej číslo!")
        c = input("Zadej konstantní člen>")
c = float(c)

def najdiKoren(a,b,c):
    d = pow(b, 2) - 4*a*c
    if d < 0:
        return "0 řešení"
    else:
        x1 = (-b + math.sqrt(d))/(2*a)
        x2 = (-b - math.sqrt(d))/(2*a)
        if x1 == x2:
            return f"1 řešení: x = {x1}"
        else:
            return f"2 řešení: (x1, x2) = ({x1}, {x2})"

print(najdiKoren(a,b,c))