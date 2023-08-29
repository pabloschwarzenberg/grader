#Ordenar tres números
while True:
    try:
        entrada = int(input("Ingrese 3 números enteros: "))
        #cadena = int(entrada)
        if len(str(entrada)) == 3:
            cadena = str(entrada)            
            
            ordena_cadena = sorted(cadena)
            cadena_final = ",".join(ordena_cadena)
            print("Los números ordenados de menor a mayor son: ", cadena_final)        
    except ValueError:                
        respuesta=input("Por Favor ingrese 3 números enteros: ")
        if respuesta=="n":
            break