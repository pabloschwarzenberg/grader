#Descomponer un número
numero=int(input("ingrese un numero de 4 cifras "))
M=numero//1000
C=(numero//100-M*10)
D=(numero//10-M*100-C*10)
U=(numero-M*1000-C*100-D*10)
print(M,"M +",C,"C +",D,"D +",U,"U")