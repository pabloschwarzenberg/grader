def obtener_subcadenas_unicas(cadena, n):
    
    frecuencias = {}
   
    for i in range(len(cadena) - n + 1):
        subcadena = cadena[i:i + n]
        if subcadena in frecuencias:
            frecuencias[subcadena] += 1
        else:
            frecuencias[subcadena] = 1
    
    subcadenas_unicas = [subcadena for subcadena, frecuencia in frecuencias.items() if frecuencia == 1]

    return subcadenas_unicas

cadena = input("Ingrese la cadena de texto: ")
n = int(input("Ingrese el valor de n: "))

subcadenas = obtener_subcadenas_unicas(cadena, n)

if len(subcadenas) > 0:
    for subcadena in subcadenas:
        print(subcadena)
else:
    print("ninguna")