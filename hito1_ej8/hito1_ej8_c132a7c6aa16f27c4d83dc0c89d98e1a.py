#descomponer un numero
numero = int(input("Número natural de 1,2,3 o 4 cifras: "))

if 0<numero<10000:

    mil = numero//1000

    centena = (numero%1000)//100

    decena = ((numero%1000)%100)//10

    unidad = ((numero%1000)%100)%10

    print(mil,"M +",centena,"C +",decena,"D +",unidad,"U")

else:
    print("Debe ser un número de hasta 4 cifras")