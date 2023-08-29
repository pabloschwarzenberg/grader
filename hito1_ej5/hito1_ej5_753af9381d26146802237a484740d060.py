#Cálculo del dígito verificador de un rut
rut = int(input("Ingresa el rut: "))
a = (rut//10000000) * 3
b = ((rut//1000000)%10) * 2
c = ((rut//100000)%10) * 7
d = ((rut//10000)%10) * 6
e = ((rut//1000)%10) * 5
f = ((rut//100)%10) * 4
g = ((rut//10)%10) * 3
h = ((rut//1)%10) * 2
Suma = (a+b+c+d+e+f+g+h)
Resto1 = Suma//11
Resto2 = Suma - (11*Resto1)
Resta = 11 - Resto2
if(Resta == 11):
  print("dv =", end ="")
  print(0)
elif(Resta == 10):
  print("dv =", end ="")
  print("k")
else:
  print("dv =", end ="")
  print(Resta)