#Descomponer un número 
 

a = int(input("escribe un numero:"))

UNIDAD=(a%10)
a//=10
DECENA=(a%10)
a//= 10
CENTENA=(a%10)
a//=10
MIL=(a%10)
a//=10

print(MIL,"M","+",CENTENA,"C","+",DECENA,"D","+",UNIDAD,"U")

