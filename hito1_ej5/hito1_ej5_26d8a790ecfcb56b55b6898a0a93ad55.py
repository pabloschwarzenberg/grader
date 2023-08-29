#Matías
#20787606
rut= int(input("Ingrese su rut sin puntos, sin comas y sin el digito verificador : ", ))
a= (rut%10)
b= ((rut%100)//10)
c=((rut%1000)//100)
d=((rut%10000)//1000)
e=((rut%100000)//10000)
f=((rut%1000000)//100000)
g=((rut%10000000)//1000000)
h=(rut//10000000)
A= a*2
B= b*3
C= c*4
D= d*5
E= e*6
F= f*7
G= g*2
H= h*3
suma= int(A+B+C+D+E+F+G+H)
divi= (suma//11)
tot= (suma - (11*divi))
resta = 11 - tot 
if (resta == 10):
  print("dv = k")
if (resta == 11):
  print("dv = 0")
else:
  print("dv =",(resta))
