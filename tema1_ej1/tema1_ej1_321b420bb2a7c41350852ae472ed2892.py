#Suma de los N primeros números

comprobar = True

while comprobar == True:

    n = int(input("ingrese un numero naural:"))

    if n > 0:

        comprobar = False
        
        resultado = 0
        
        for i in range(1,n+1):
        
            resultado = (i * (i +1)) / 2

        print("el resultado de la seie es:", resultado)

    else:
        print("el numero ingresado no es correcto")
