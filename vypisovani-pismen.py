str = input("Napiš až 15 písmen >")
while len(str) > 15 or str.isalpha() == False:
        print("Maximálně 15 písmen!")
        str = input("Napiš až 15 písmen >")
abc = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
for pismeno in str:
    i = abc.index(pismeno) + 1
    line = pismeno * i
    print(line)
