#Descomponer un número
n = int(input("insertar un numero: "))
M = (n //1000)
C = int(n/100)%10
D = (n% 100)//10
U = n%10
print(M,"M", "+", C,"C", "+", D,"D", "+", U,"U")
