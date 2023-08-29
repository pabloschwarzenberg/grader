#Descomponer un número
numero = int (input ('Ingresa el valor de numero: '))

milesimas = (numero%10000-numero%1000)//1000
centenas = (numero%1000-numero%100)//100
decenas = (numero%100-numero%10)//10
unidades = numero%10

print("La descomposicion de su numero es la siguiente: ")

if (milesimas==0 and centenas==0 and decenas==0 and unidades>=0) :
    print (unidades,"D")
    
elif (milesimas==0 and centenas==0 and decenas>=0 and unidades>=0) :
    print (decenas,"D","+", unidades,"U")

elif (milesimas==0 and centenas>=0 and decenas>=0 and unidades>=0) :
    print (centenas,"C","+", decenas,"D", "+", unidades,"U")
    
    
else: print(milesimas,"M","+",centenas,"C","+",decenas,"D","+",unidades,"U")
