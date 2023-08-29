#Ordenar tres números
#solicitar numeros a ordenar
numero1=int(input("Ingrese el primer numero: "))
numero2=int(input("Ingrese el segundo numero: "))
numero3=int(input("ingrese el tercer numero: "))

#operacion
if numero1 <= numero2 and numero1 <= numero3:
    primero = numero1
    if numero2 <= numero3:
        segundo = numero2
        tercero = numero3
    else:
        segundo = numero3
        tercero = numero2
elif numero2 <= numero1 and numero2 <= numero3:
    primero = numero2
    if numero1 <= numero3:
        segundo = numero1
        tercero = numero3
    else:
        segundo = numero3
        tercero = numero1
else:
    primero = numero3
    if numero1 <= numero2:
        segundo = numero1
        tercero = numero2
    else:
        segundo = numero2
        tercero = numero1

#mensaje final
print("Los numeros ordenados son:", primero, ",", segundo, ",", tercero)
