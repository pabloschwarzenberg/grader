#Sistema de Ecuaciones
#primera ecuacion
# ax +by = c
#import round
a = float(input("ingrese primer numero: "))   
b = float(input("ingrese segundo numero: "))   
c = float(input("ingrese tercero numero: "))   
#segunda ecuacion
# dx + fy = g
d = float(input("ingrese cuarto numero: "))   
f = float(input("ingrese quinto numero: "))   
g = float(input("ingrese sexto numero: "))

y = (c-(a*g)/d)/(((-a*f)/d)+b)

x = (c-b*y)/a

x = round(x,1)
y = round(y,1)

print("x="+str(x))
print("y="+str(y))