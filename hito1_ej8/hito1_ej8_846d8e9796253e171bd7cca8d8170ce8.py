numero = input("Ingresa un número de hasta 4 dígitos: ")

if numero.isdigit() and len(numero) <= 4:
    numero = numero.zfill(4)
    unidades = numero[3]
    decenas = numero[2]
    centenas = numero[1]
    miles = numero[0]

    output = ""
    if miles != "0":
        output += miles + "M+"
    if centenas != "0":
        output += centenas + "C+"
    if decenas != "0":
        output += decenas + "D+"
    output += unidades + "U"

    print("Descomposición:", output)
else:
    print("Error: Ingresa un número válido de hasta 4 dígitos.")
