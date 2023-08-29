A=float(input("ingresa Coef. X1: "))
B=float(input("ingresa Coef. Y1: "))
C=float(input("ingresa Coef. 1: "))

D=float(input("ingresa Coef. X2: "))
E=float(input("ingresa Coef. Y2: "))
F=float(input("ingresa Coef. 2: "))

primero=(A*E/B)
segundo=(B*E/B)
tercero=(C*E/B)
cuarto= primero-D
quinto=segundo-E
sexto=tercero-F
X=sexto/cuarto
Y=(C-A*X)/B

print("X= ",X)
print("Y= ",Y)