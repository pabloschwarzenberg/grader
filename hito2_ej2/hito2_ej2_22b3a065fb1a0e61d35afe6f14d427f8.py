string = str(input("ingrese palabra"))
for i in string:
    genoma = "actgACTG"
    if i in genoma:
        print("secuencia correcta")
    else:
        print("secuencia incorrecta")
        