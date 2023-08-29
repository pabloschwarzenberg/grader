#Descomponer un número
numero = eval(input("Ingrese un numero de 4 cifras: "))

milesima = numero // 1000
numero = numero % 1000
centena = numero // 100
numero = numero % 100
decena = numero // 10
numero = numero % 10
unidad = numero

if milesima == 0:
    if centena == 0:
        if decena == 0:
            print(unidad,"U")
        else:
            print(decena,"D + ",unidad,"U")
    else:
        print(centena,"C + ",decena,"D + ",unidad,"U")

else:
    print(milesima,"M + ",centena,"C + ",decena,"D + ",unidad,"U")
    
     