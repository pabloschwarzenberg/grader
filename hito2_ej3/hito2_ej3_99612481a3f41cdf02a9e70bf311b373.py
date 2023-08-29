codon = input("Ingrese la secuencia: ")
n = int(input("Ingrese el numero: "))
posibles_combinaciones = [codon[i:i+n] for i in range(len(codon) - 2)]
for cod in posibles_combinaciones:
    if posibles_combinaciones.count(cod) != 1:
        posibles_combinaciones = list(filter(lambda a: a != cod, posibles_combinaciones))

if len(posibles_combinaciones) == 0:
    print("ninguna")
else:
    for cod in posibles_combinaciones:
        print(cod)