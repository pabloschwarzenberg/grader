secuencia = input("Escriba la secuencia: ")
for carac in secuencia:
    if carac == "A" and carac == "C" and carac == "T" and carac == "G":
        print("secuencia correcta")
    elif carac == "a" and carac == "c" and carac == "t" and carac == "g":
        print("secuencia correcta")
    else:
        print("secuencia incorrecta")