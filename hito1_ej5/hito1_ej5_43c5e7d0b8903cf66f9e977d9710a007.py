#Cálculo del dígito verificador de un rut
print("Ingresar Rut sin guion: ")
rut=int(input())
A=((rut%10)*2)
B=(((rut%100)//10)*3)
C=(((rut%1000)//100)*4)
D=(((rut%10000)//1000)*5)
E=(((rut%100000)//10000)*6)
F=(((rut%1000000)//100000)*7)
G=(((rut%10000000)//1000000)*2)
H=(((rut%100000000)//10000000)*3)

I=(A+B+C+D+E+F+G+H)
J=(I//11)
K=I-(11*J)
L=(11-K)

if (L==11):
 print("dv=", end="")
 print(0)
elif (L==10):
 print("dv=", end="")
 print("k")
else:
 print("dv=", end="")
 print(L)
