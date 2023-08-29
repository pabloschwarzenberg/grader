#Descomponer un número
n = eval(input("ingrese un numero de 4 digitos"))
M= n//1000
C = (n - (M*1000))//100
D = (n - (M*1000)-(C*100))//10
U = (n - (M*1000)-(C*100)-(D*10))//1
if M > 0 and C > 0 and D > 0 and U > 0:
    print(M, "M +", C, "C +", D, "D +", U, "U")
elif C > 0 and D > 0 and U > 0:
    print(C, "C +", D, "D +", U, "U")
elif D > 0 and U > 0:
    print(D, "D +", U, "U")
elif U > 0:
    print(U, "U")
else:
    print("ingrese un nuevo numero")     