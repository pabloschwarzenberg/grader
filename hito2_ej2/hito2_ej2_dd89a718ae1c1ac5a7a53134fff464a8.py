genoma = ["A", "C", "T", "G"]

gen = str.upper(input("Ingrese la secuencia: "))

if len(gen) == 4:
    if gen[0] == "A" and gen[1] == "C" and gen[2]== "T" and gen[3] == "G":
        print("secuencia correcta")
    else:
        print("secuencia incorrecta")
else:
    print("secuencia incorrecta")