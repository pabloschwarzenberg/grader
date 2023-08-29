#Descomponer un número
numero_natural = int(input("numero natural de 1,2,3 o 4 cifras:"))

if numero_natural > 0:
    numero_mil = numero_natural//1000
    centena_numero = (numero_natural%1000)//100
    decena_numero = ((numero_natural%1000)%100)//10
    unidad_numero = ((numero_natural%1000)%100)%10
    print(str(numero_mil)+"M + "+str(centena_numero)+"C + "+str(decena_numero)+"D + "+str(unidad_numero)+"U")
    
else:
     print("debe ser un numero de hasta 4 cifras")      