#importuje knihovnu matematika pro zjednodušení a zpřesnění matematických operací
import math

#vstup hodnot
print("pracujeme se vzorcem ax^2 + bx + c = 0")

a=input("zadejte a")
try:
    ao=str(int(a)**2)
except:
    print("zadejte číslo")
    quit()
    
b=input("zadejte b")
try:
    bo=str(int(b)**2)
except:
    print("zadejte číslo")
    quit()
    
c=input("zadejte c")
try:
    co=str(int(c)**2)
except:
    print("zadejte číslo")
    quit()
    
#převedení na integer
a=int(a)
b=int(b)
c=int(c)

#výpočet diskriminantu
d=(b**2)-4*a*c
print("diskriminant "  + str(d))

#lineární rovnice
if a==0:
    x = (-c)/b
    print("x = " + str(x))
    input("stisknutím klávesy ukončíte program")
    exit()
    
#počet kořenů
if d>0:
    k=2
elif d==0:
    k=1
else:
    k=0
print("počet kořenů " + str(k))


#výpočet kořenů s rozhodnutím o počtu + vyplivnutí výsledku
if k==0:
    print("rovnice nemá žádné reálné řešení")
elif k==1:
    x = (-b)/(2*a)
    print("x = " + str(x))
else:
    x1 = (math.sqrt(d)-b)/(2*a)
    x2 = (-(math.sqrt(d))-b)/(2*a)
    print("x1 = " + str(x1))
    print("x2 = " + str(x2))

#výpočet kořenů
#x1 = (-b + math.sqrt(d))/(2*a)
#x2 = (-b - math.sqrt(d))/(2*a)
