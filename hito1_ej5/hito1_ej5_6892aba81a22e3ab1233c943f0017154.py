#Cálculo del dígito verificador de un rut
rut = input("Ingrese número del RUT:")
largo = len(rut)
m=1
s=0
for i in range(largo-1,-1,-1):
    m = m+1
    s = s + int(rut[i])*m
    if (m ==7):
        m = 1
#print(s)
r=s%11
#print(r)
dv=11-r
#print(dv)
if dv == 11:
    dv = "0"
if dv == 10:
    dv = "K"
print("dv=", dv)