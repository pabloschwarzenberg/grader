#ORDENAR 3 NUMEROS DE MENOR A MAYOR

#ENTRADA
numero_a = int(input('Ingrese un numero entero: '))
numero_b = int(input('Ingrese un segundo numero entero: '))
numero_c = int(input('Ingrese un tercer numero entero: '))


#PROCESAMIENTO

if numero_a > numero_b and numero_a > numero_c :
    mayor = numero_a
    if numero_b > numero_c :
        medio = numero_b
        menor = numero_c
    else : 
        medio = numero_c
        menor = numero_b
elif numero_b > numero_a and numero_b > numero_c :
    mayor = numero_b
    if numero_a > numero_c :
        medio = numero_a
        menor = numero_c
    else : 
        medio = numero_c
        menor = numero_a
else :
    mayor = numero_c
    if numero_a > numero_b :
        medio = numero_a
        menor = numero_b
    else : 
        medio = numero_b
        menor = numero_a

#SALIDA
print('Orden de menor a mayor: ', menor,',',medio,',',mayor)