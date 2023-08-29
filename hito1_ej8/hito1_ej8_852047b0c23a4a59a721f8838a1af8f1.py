#Descomponer un número
n = int(input())
U = n%10
D = (n//10)%10
C = (n//100)%10
M = (n//1000)%10
if M > 0:
    print(M,'M + ', C,'C + ', D,'D + ', U,'U')
elif C > 0:
    print(C,'C + ', D,'D + ', U,'U')
elif D > 0:
    print(D,'D + ', U,'U')
else:
    print(U,'U')     