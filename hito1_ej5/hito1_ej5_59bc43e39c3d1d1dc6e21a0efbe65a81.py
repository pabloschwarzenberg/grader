#Cálculo del dígito verificador de un rut
rut = int(input("Ingrese su rut sin puntos, guión ni digito verificador: "))
a = (rut//10000000)
b = (rut//1000000) % 10
c = (rut//100000) % 10
d = (rut//10000) % 10
e = (rut//1000) % 10
f = (rut//100) % 10
g = (rut//10) % 10
h = (rut//1) %10 

A = h*2
B = g*3
C = f*4
D = e*5
E = d*6
F = c*7
G = b*2
H = a*3

SP = (A + B + C + D + E + F + G + H)
RD = SP % 11
X = 11 - RD

if (X==11):
    print("dv = 0")
elif (X==10):
    str(print("dv = K"))
else:
    print("dv = ", X,)
        

