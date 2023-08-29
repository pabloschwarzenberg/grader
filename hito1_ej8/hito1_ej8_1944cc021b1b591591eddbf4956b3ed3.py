#Descomponer un número
print("Introduce el número: ")
numero = int(input ())

mil = (numero%10000-numero%1000)//1000

centenas =(numero%1000-numero%100)//100

decenas =(numero%100-numero%10)//10
unidades = numero%10


if numero > 9999:
    print('numero no valido')
    
elif numero >= 1000 and numero <= 9999:
    print(mil,"M","+",centenas,"C","+", decenas,"D","+", unidades,"U")
    
elif numero >= 100 and numero <= 999:
    print(centenas,"C","+", decenas,"D","+", unidades,"U")
    
elif numero >= 10 and numero <= 99:
    print(decenas,"D","+", unidades,"U")
    
elif numero <= 9:
    print(unidades)