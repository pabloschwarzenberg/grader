rut= input("Ingrese el rut")

if len(rut) < 8:
    rut = "0"+rut
    
else:
    rut=rut

rut=rut.lower()

a=int(rut[7])
b=int(rut[6])
c=int(rut[5])
d=int(rut[4])
e=int(rut[3])
f=int(rut[2])
g=int(rut[1])
h=int(rut[0])

a= a*2
b= b*3
c= c*4
d= d*5
e= e*6
f= f*7
g= g*2
h= h*3

suma= (a+b+c+d+e+f+g+h)
sumas= suma//11
sumass= suma-(11*sumas)
dv= (11-sumass)

if dv==11:
    dv=0
    print("dv=",dv)
    
if dv==10:
    dv="k"
    print("dv=",dv)
    
print("dv=",dv)
