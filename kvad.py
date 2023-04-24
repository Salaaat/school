def count(a, b, c):
    promenne = [a, b, c]
    for idx, i in enumerate(promenne):
        if not i:
            return "Priste prosim se vstupem", ''
        if i[0] == "-":
            kladne = False
            i = i.split("-")[1]
        else:
            kladne = True
        try:
            i = int(i)
        except ValueError as err:
            return f"Tobe by se taky nechtelo pocitat s {i},\nrozumnejsi zadani by nebylo?", ''
        if not kladne:
            i = -i
        promenne[idx] = i
    a, b, c = promenne
    d = b**2 - 4*a*c
    reseni = None
    if d < 0:
       return 'Nema reseni', ''
    e = d**0.5
    x = (-b + e) / 2*a
    y = (-b - e) / 2*a
    koreny = [x, y]
    if d == 0:
        reseni = 1
        return "Drumroll, pls! Koren:", x
    else:
        reseni = 2
        return "Koreny:", x, y, "Nz ;)"

while True:
    print(*count(input("a = "), input("b = "), input("c = ")))
