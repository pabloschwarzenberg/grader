#Descomponer un número
n = int(input("NUMERO: "))
M = n//1000
C = (n%1000)//100
D = ((n%1000)%100)//10
U = (((n%1000)%100)%10)
print(M, " M + ", C, " C + ", D,  " D + ", U, " U")