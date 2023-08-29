#Descomponer un número
numero= int(input("Ingrese numero de hasta 4 digitos: "))

M= numero//1000
C= ((numero//100)%10)
D= ((numero//10)%10)
U= (numero%10)
print(numero)
print(M,"M +",C,"C +",D,"D +", U,"U")   
      