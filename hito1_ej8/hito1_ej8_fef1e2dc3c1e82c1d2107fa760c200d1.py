#Descomponer un número
numero=int(input("Ingresa un numero"))
Unidad=numero%10

Decena=numero//10
Decena=Decena%10

Centena=numero//100
Centena=Centena%10

Miles=numero//1000
Miles=Miles%10

print(Miles,"M +",Centena,"C +",Decena,"D +",Unidad,"U")