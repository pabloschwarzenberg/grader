#Cálculo del dígito verificador de un rut
 
  rut= int(input("Ingresa un rut sin digito verificador: "))
rut= str(rut)
#1234567
a= rut[6]
a=int(a)*2

b= rut[5]
b=int(b)3

c= rut[4]
c_=int(c)4

d= rut[3]
d=int(d)*5

e= rut[2]
e=int(e)6

f= rut[1]
f_=int(f)7

g= rut[0]
g=int(g)*2

suma= a+b+c+d+e+f+g
entera= suma//11
resto= suma-(11*entera)
ver= 11-resto
dig_v= 0
if ver==11:
    dig_v= 0
elif ver==10:
    dig_v= k
else:
    dig_v= ver
    dig_v=str(dig_v)
print("dv= ", dig_v)