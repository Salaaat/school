#užitečná zavedení
abc=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
i=0

#input, ověření
vstup=input("vložte až patnáct písmen anglické abecedy")

a=list(vstup)

while len(a)>15:
    vstup=input("vložte maximálně 15 písmen")
    a=list(vstup)

#print písmen
while i<len(a):
    x=abc.index(a[i])+1
    c=x-1

    print(abc[c]*x)
    
    i+=1
