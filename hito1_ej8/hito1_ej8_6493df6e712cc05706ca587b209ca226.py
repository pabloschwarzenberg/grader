#Descomponer un número
n = int(input("Ingresa un numero de cuatro digitos o menos: "))

if 0 < n <10000:
   M = n // 1000
   C = (n%1000)//100
   D = ((n%1000)%100)//10
   U = ((n%1000)%100)%10
   print(M,"M +",C,"C +",D,"D +",U,"U")
else:
   print("Debe ser un numero hasta 4 cifras")      