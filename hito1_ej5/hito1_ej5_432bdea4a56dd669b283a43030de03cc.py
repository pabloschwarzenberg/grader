#Cálculo del dígito verificador de un rut
rut=input("Ingrese su rut: ")
rut=list(rut)
for i in range(len(rut)):
  rut[i]=int(rut[i])
coef=[3,2,7,6,5,4,3,2]
x=0
for j in range(0,7):
  x+=(coef[j])*(rut[j])
resto=x%11
dv=11-resto
if dv==11:
   dv=="0"
if dv == 10:
  dv="k"
else:
  dv=str(dv)
dv="dv="+dv
print(dv)