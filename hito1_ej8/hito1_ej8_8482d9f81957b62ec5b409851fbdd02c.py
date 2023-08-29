#Descomponer un número
numero=eval (input("Ingrese un número inferior a 10.000 : "))



M =(numero//1000) %10
C =(numero//100)%10
D =(numero//10)%10
U =(numero//1)%10

print(M,"M+",C,"C+",D,"D+",U,"U",)

     