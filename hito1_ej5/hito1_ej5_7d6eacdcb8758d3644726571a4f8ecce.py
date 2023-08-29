rut = input(" Ingrese n° de rut sin digito verificador: ")
rut = int(rut)
a = rut % 10
a1 = 2*a 
b = ((rut % 100)- a)/10
b1 = 3*b 
c = ((rut % 1000) - (rut%100))/100
c1 = 4*c
d = ((rut % 10000) - (rut%1000))/1000
d1 = 5*d
e = ((rut % 100000) - (rut%10000))/10000
e1 = 6*e
f = ((rut % 1000000) - (rut%100000))/100000
f2 = 7*f
g = ((rut % 10000000) - (rut%1000000))/1000000
g1 = 2*g
h = ((rut % 100000000) - (rut%10000000))/10000000
h1 = 3*h
s = a1 + b1 + c1 + d1 + e1 + f2 + g1 + h1
k = s//11 
o = s - (11*k)
u = 11 - o 
if u==11:
 print("dv=0")
elif u==10:
 print("dv=K")
else:
   print("dv=" + str(u))
    
   