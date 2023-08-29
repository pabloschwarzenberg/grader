#Descomponer un número

numero = int(input("Número natural de 1,2,3 o 4 cifras: "))

if 0<numero<10000:
    mil = numero//1000
    cien = (numero%1000)//100
    diez  = ((numero%1000)%100)//10
    uno = ((numero%1000)%100)%10
    print(mil,"M +",cien,"C +",diez,"D +",uno,"U")
else:
    print("Invalido")
