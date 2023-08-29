#Descomponer un número
num=int(input("Ingrese un numero de 4 digitos:"))

UM=num//10**3
C=(num//10**2)%10**1
D=(num//10**1)%10**1
U=num%10**1

print(str(UM)+"M","+",str(C)+"C","+",str(D)+"D","+",str(U)+"U")