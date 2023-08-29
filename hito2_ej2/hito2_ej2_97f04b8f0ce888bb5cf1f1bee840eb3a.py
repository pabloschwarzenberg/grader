X = input("Ingrese su secuancia de ADN: ")

Lista = ["A","C","T","G","a","c","t","g"]

Error = False

for Letra in X:
    if Letra not in Lista:
        print("La secuencia", X, "es incorrecta")
        Error = True
        break

if Error == False:
    print("La secuencia", X, "es correcta")