#Ordenar tres números

#ENTRADA
numero1 = int(input("ingrese el primer numero: "))
numero2 = int(input("ingrese el segundo numero: "))
numero3 = int(input("ingrese el tercer numero: "))

#PROCESO
#si  el primer numero ingresado es mayor
if (numero1 > numero2) and (numero1 > numero3):
    mayor = numero1
    if numero2 > numero3:
        medio = numero2
        menor = numero3
    else:
        medio = numero3
        menor = numero2

#si  el segundo numero ingresado es mayor        
elif (numero2 > numero3):
    mayor = numero2
    if numero1 > numero3:
        medio = numero1
        menor = numero3
    else:
        medio = numero3
        menor = numero1

#si  el tercer numero ingresado es mayor
else:
    mayor = numero3
    if numero1 > numero2:
        medio = numero1
        menor = numero2
    else:
        medio = numero2
        menor = numero1

#SALIDA
print(str(menor)+ ", " + str(medio) + ", " + str(mayor)) 