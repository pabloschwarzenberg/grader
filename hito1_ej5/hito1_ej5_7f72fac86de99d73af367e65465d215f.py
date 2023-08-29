rut=int(input("favor ingrese su rut: "))
a=rut//10000000
restoa=rut%10000000
b=restoa//1000000
restob=restoa%1000000
c=restob//100000
restoc=restob%100000
d=restoc//10000
restod=restoc%10000
e=restod//1000
restoe=restod%1000
f=restoe//100
restof=restoe%100
g=restof//10
h=restof%10

H=h*2
G=g*3
F=f*4
E=e*5
D=d*6
C=c*7
B=b*2
A=a*3

suma=H+G+F+E+D+C+B+A
restosuma=suma%11
resultado=11-restosuma
if resultado == 11:
    print("dv=",0)
elif resultado == 10:
    print ("dv=","K")
else:
    print("dv=",resultado)
