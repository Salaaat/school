input_str = input("Zadejte řetězec (max. 15 písmen):tobias")

# Omezení délky řetězce na maximálně 15 písmen
input_str = input_str[:15]

# Roztřídění písmen vstupního řetězce podle abecedy
sorted_str = sorted(input_str)

# Vypsání každého písmene tolikrát, na kolikátém místě je v abecedě
for char in sorted_str:
    index = ord(char.lower()) - 97 + 1
    print(char * index)
