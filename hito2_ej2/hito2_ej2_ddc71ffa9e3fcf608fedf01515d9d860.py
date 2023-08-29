intento = input("Ingrese secuencia: ")
intento = intento.upper()
for letra in intento:
    if letra not in "ACTG":
        print("secuencia incorrecta")
        
    if letra in "ACTG":
        print("secuencia correcta")