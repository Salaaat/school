import math
#zadání stran (a) a (b) + [ověření]
a=input("zadejte celočíselnou stranu a")
if not(a.isdigit()):
    print("vložte celé číslo")
    quit()
b=input("zadejte celočíselnou stranu b")
if not(b.isdigit()):
    print("vložte celé číslo")
    quit()
    
#strany
c=math.sqrt((int(a)**2)+(int(b)**2))
print("a:"+a)
print("b:"+b)
print("c:"+str(c))

#obvod
o=int(a)+int(b)+int(c)
print("obvod:"+str(o))

#obsah
s=int(a)*int(b)/2
print("obsah:"+str(s))
