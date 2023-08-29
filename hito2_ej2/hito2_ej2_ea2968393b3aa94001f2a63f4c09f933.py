secuence = input("Ingrese secuencia: ")
for letra in secuence:
    if not letra.lower() in "actg":
        print("secuencia incorrecta")
        break
print("secuencia correcta")     