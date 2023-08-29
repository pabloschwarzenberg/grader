genoma = input("Ingrese su cadena: ")
resultado = ""
for i in genoma:
    if i == ",":
        pass
    elif i == "a" or i == "A" or i == "c" or i == "C" or i == "t" or i == "t" or i == "g" or i == "G":
        resultado = "secuencia correcta"
    else:
        resultado = "secuencia incorrecta"

print(resultado)
