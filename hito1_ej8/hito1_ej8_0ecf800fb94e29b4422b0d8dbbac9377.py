#Descomponer un número
numero=int(input("ingrese un numero: "))
M=(numero//1000%10)
C=(numero//100%10)
D=(numero//10%10)
U=(numero%10)
print(M,"M +",C,"C +",D,"D +",U,"U")