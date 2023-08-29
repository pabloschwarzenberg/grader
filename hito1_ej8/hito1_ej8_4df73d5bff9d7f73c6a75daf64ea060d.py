#Descomponer un número
Numero = int(input("Ingrese numero de hasta 4 digitos"))


M = Numero//1000
C = (Numero%1000)//100
D = (Numero%100)//10
U =(Numero%10)

M = str(M)
C = str(C)
D = str(D)
U = str(U)



print(M + str("M"), "+", C + str("C"), "+", D + str("D"), "+", U + str("U"))

