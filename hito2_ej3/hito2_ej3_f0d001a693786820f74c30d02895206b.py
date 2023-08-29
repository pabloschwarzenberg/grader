def encontrar_subcadenas_unicas(cadena, n):
    subcadenas = []
    contador = {}
    
   
    for i in range(len(cadena) - n + 1):
        subcadena = cadena[i:i+n]
        
        
        if subcadena in contador:
            contador[subcadena] += 1
        else:
            contador[subcadena] = 1
            
   
    for subcadena, apariciones in contador.items():
        if apariciones == 1:
            subcadenas.append(subcadena)
            
    return subcadenas


cadena = input("Ingrese la cadena: ")
n = int(input("Ingrese el valor de n: "))


subcadenas_unicas = encontrar_subcadenas_unicas(cadena, n)
for subcadena in subcadenas_unicas:
    print(subcadena)      