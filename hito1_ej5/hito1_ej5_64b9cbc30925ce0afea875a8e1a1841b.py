#Cálculo del dígito verificador de un rut
rut=int(input("ingrese su rut"))
a=2
def reverse(num):
  return str(num)[::-1]
rut=reverse(rut)
i=0
numerito=0
d=0
for i in range(0,len(str(rut))):
    if a==8:
        a=2
    numerito=int(str(rut)[i])*a
    d=d+numerito
    a=a+1
f=d%11
dv=11-f
if dv==11:
    dv=0
elif dv==10:
    dv="K"
print("dv="+str(dv))
