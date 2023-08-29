#Cálculo del dígito verificador de un rut
rut=input("Escribe tu rut:" )

if len(rut)==(7):
   rut= "0"+ rut
 
a=int(rut[0])*3
b=int(rut[1])*2
c=int(rut[2])*7
d=int(rut[3])*6
e=int(rut[4])*5
f=int(rut[5])*4
g=int(rut[6])*3
h=int(rut[7])*2

i=(a+b+c+d+e+f+g+h)
resto=(i%11)
l=(11-resto)

if l==10:
   print ("dv=k")
elif l==11:
   print ("dv=0")
else:
   print ("dv=", l )  