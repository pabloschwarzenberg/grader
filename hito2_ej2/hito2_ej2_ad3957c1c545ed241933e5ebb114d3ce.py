lista = []

letras = input("Ingrese secuencia: ")
letras.split(";")
lista.append(letras)

if letras == "A" or letras == "a":
    print("Secuencia correcta")
elif letras == "C" or letras == "c":
    print("Secuencia correcta")
elif letras == "T" or letras == "t":
    print("Seuencia correcta")
elif letras == "G" or letras == "g":
    print("Secuencia correcta")
else:
    print("Secuencia incorrecta")