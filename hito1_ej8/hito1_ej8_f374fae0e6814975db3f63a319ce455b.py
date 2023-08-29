#Descomponer un número
numero = input("Ingrese un número de hasta 4 dígitos: ")

if len(numero) > 4:
    print("El número ingresado tiene más de 4 dígitos.")
else:
    descomposicion = []
    
    if len(numero) == 4:
        descomposicion.append(numero[0] + "M")
        
    if len(numero) >= 3:
        descomposicion.append(numero[-3] + "C")
        
    if len(numero) >= 2:
        descomposicion.append(numero[-2] + "D")
        
    descomposicion.append(numero[-1] + "U")
    
    print(" + ".join(descomposicion))
      