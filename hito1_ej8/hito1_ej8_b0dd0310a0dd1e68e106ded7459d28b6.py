#Descomponer un número
M=1000
C=100
D=10
U=1
a=int(input("ingrese número de 4 dígitos: "))
m=int(a//1000)
mM=m*M
c=int((a-mM)//100)
cC=c*C
d=int(((a-(mM+cC))//10))
dD=d*D
u=int(((a-(mM+cC+dD))//1))
print(m,"M", "+", c, "C", "+", d, "D", "+", u, "U")    