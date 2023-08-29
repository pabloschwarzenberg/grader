#Cálculo del dígito verificador de un rut
rut= int(input("Ingrese rut: "))
a=rut//10000000 * 3
b=(rut//1000000)%10 * 2
c=(rut//100000)%10 * 7
d=(rut//10000)%10 * 6
e=(rut//1000)%10 * 5
f=(rut//100)%10 * 4
g=(rut//10)%10 * 3
h=(rut//1)%10 * 2
S=(a+b+c+d+e+f+g+h)
A= S // 11
B= S-(11*A)
C= 11-B

if C == 11:
  print("DV = 0")

elif C == 10:
  print("DV = K")

else:
  print("DV = ",C)     