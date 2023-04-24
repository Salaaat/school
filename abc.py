def printer(word):
    if len(word) > 15:
        return "max 15 pls"
    abc = []
    for i in "abcdefghijklmnopqrstuvwxyz":
        abc.append(i)
    abc = tuple(abc)
    for i in word:
        print(i*(abc.index(i)-1))

while True:
    printer(input())
