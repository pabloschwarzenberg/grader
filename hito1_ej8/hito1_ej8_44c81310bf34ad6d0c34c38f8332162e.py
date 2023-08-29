#Descomponer un número
x=int(input("ingrese un numero:"))

unidades= x%10;
x= x//10;
decenas= x%10;
x=x//10;
centenas=x%10;
um=x//10
print(um,"M","+",centenas,"C","+",decenas,"D","+",unidades,"U")
