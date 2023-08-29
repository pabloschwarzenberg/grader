x = int(input("ingresa un numero: "))

UNIDAD=(x%10)
x//=10
DECENA=(x%10)
x//= 10
CENTENA=(x%10)
x//=10
MIL=(x%10)
x//=10

print(MIL,"M","+",CENTENA,"C","+",DECENA,"D","+",UNIDAD,"U")

         
