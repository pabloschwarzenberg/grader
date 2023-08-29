numero = input("Ingrese un número de hasta 4 dígitos: ")

if len(numero) > 4:
    print("El número ingresado tiene más de 4 dígitos.")
else:
    unidades = int(numero[-1])
    decenas = int(numero[-2]) if len(numero) >= 2 else 0
    centenas = int(numero[-3]) if len(numero) >= 3 else 0
    miles = int(numero[-4]) if len(numero) == 4 else 0
    
    resultado = []
    
    if miles != 0:
        resultado.append(f"{miles}M")
    
    if centenas != 0:
        resultado.append(f"{centenas}C")
    
    if decenas != 0:
        resultado.append(f"{decenas}D")
    
    resultado.append(f"{unidades}U")
    
    print(" + ".join(resultado))
