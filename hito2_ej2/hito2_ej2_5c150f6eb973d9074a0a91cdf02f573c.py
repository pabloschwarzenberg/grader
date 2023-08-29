secuencia = input("Ingrese secuencia: ")
for letra in secuencia:
    if not letra.lower() in "actg":
        print("secuencia incorrecta")
        break
print("secuencia correcta")
      