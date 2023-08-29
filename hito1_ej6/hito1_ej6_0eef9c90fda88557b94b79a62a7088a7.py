#Ordenar tres números
numero1 = int(input("Ingresa el primer numero: "))
numero2 = int(input("Ingresa el segundo numero: "))
numero3 = int(input("Ingresa el tercer numero: "))

menor = 0
medio = 0
mayor = 0 

if numero1 < numero2 and numero1 < numero3:
    menor = numero1
    if numero2 < numero3:
        medio = numero2
        mayor = numero3
    else:
        mayor = numero2
        medio = numero3
if numero2 < numero1 and numero2 < numero3:
    menor = numero2
    if numero1 < numero3:
        medio = numero1
        mayor = numero3
    else:
        mayor = numero1
        medio = numero3
if numero3 < numero2 and numero3 < numero1:
    menor = numero3
    if numero2 < numero1:
        medio = numero2
        mayor = numero1
    else:
        mayor = numero2
        medio = numero1
menor =str(menor)
medio =str(medio)
mayor =str(mayor)
print(menor+","+medio+","+mayor)