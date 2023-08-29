a=input("ingrese rut sin digito verificador: ")
t = 2
suma=0
for i in range(len(a)-1,-1,-1):
   suma+=int(a[i])* t
   if t==7:
      t=2
   else:
      t+=1
b=suma%11
dv=11-b
if dv==10:
   dv="k"
elif dv==11:
   dv=0
print("dv=",dv)