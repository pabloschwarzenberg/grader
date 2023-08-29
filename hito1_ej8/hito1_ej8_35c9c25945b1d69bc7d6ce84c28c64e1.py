#Descomponer un número
numero = int(input("ingrese numero a descomponer="))
M = numero//1000
C = (numero//100)%10
D = (numero%100)//10
U = numero%10

print(str(M) + str("M"),"+",str(C) + str("C"),"+",str(D) + str("D"),"+",str(U) + str("U"))
