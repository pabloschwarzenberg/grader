#Conversión de Decimal a Binario
n=int(input("ingrese numero para convertir a binario: "))
a=n//128
restoa=n%128
b=restoa//64
restob=restoa%64
c=restob//32
restoc=restob%32
d=restoc//16
restod=restoc%16
e=restod//8
restoe=restod%8
f=restoe//4
restof=restoe%4
g=restof//2
restog=restof%2
h=restog//1
if a == 1:
    A = 10000000
else:
    A = 0 
if b == 1:
    B = 1000000
else:
    B = 0
if c == 1:
    C = 100000
else:
    C = 0
if d == 1: 
    D = 10000
else:
    D = 0
if e == 1:
    E = 1000
else:
    E = 0
if f == 1:
    F = 100
else:
    F = 0
if g == 1:
    G = 10
else:
    G = 0
if h == 1:
    H = 1
else:
    H = 0
RESULTADO=A+B+C+D+E+F+G+H
print("resultado=",RESULTADO)