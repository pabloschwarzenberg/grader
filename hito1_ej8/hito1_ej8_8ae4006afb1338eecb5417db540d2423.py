#Descomponer un número
      
numero = int (input ('Ingresa el valor de numero: '))
M = (numero%10000-numero%1000)//1000
C = (numero%1000-numero%100)//100
D = (numero%100-numero%10)//10
U = numero%10

print (str(M) + "M + " + str(C) + "C + " + str(D) + "D + " + str(U) + "U ")