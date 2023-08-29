secuencia = input("Ingrese secuencia: ")
for letra in secuencia:
    if not letra.lower() in "actg":
        print("Secuencia incorrecta")
        break
print("Secuencia correcta")      