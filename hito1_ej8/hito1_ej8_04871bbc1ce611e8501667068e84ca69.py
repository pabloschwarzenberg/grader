import math
num=int(input("ingrese un numero de 4 digitos:"))
M=(num//1000)
C=(num//100)%10
D=(num//10)%10
U=(num//1)%10
uno=M
dos=C
tres=D
cuatro=U
print(uno,"M+",dos,"C+",tres,"D+",cuatro,"U")
