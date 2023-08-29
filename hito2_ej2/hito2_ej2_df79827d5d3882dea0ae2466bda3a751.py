texto = str(input("Ingrese secuencia: "))
genoma = ["A","C","T","G"]
for i in texto:
    if i in genoma:
        print("Secuencia correcta")
    if i not in genoma:
        print("Secuencia incorrecta")