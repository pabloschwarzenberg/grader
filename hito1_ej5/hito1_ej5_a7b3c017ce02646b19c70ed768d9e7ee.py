#Cálculo del dígito verificador de un rut
r=str(input("Ingrese su rut sin digito verificador ni puntos "))
l = len(r)
c=l-1
s=0
h=2
for i in range(l):
    k = (h)*int(r[c])
    s+=k
    c+=-1
    h+=1
    if h ==8:
            h =2
v=s%11
v=11-v
if v==11:
    print("dv=0")
elif v ==10:
    print("dv=k")
else:
    print("dv=",v)      