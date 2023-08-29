numero = input("Ingrese un número: ")

if not numero.isdigit():
    print("Error: ingrese un número válido.")
else:
    longitud = len(numero)

    letras = {
        1: "U",
        2: "D",
        3: "C",
        4: "M"
    }

    descomposicion = []
    for i in range(longitud):
        d = int(numero[i])
        descomposicion.append(str(d) + letras[longitud - i])

    print("Descomposición del número:")
    print("+".join(descomposicion))


