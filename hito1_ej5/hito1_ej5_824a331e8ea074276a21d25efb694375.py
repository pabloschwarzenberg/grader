#Cálculo del dígito verificador de un rut
rut=str(input("ingrese RUT sin digito verificador:"))
l=len(str(rut))
tur=rut[::-1]   
k=1
resultado=0
for i in range(l):
 
   k=k+1
   a=(int(tur[i]))*(k)
   resultado=resultado+a
   #print(tur[i],k,"=",a)
   if k>6:
    k=1      
resto=resultado//11
mult=resto*11
res=abs(resultado-mult)

dv=abs(11-res)
#print(dv)
if dv ==11:
   dv=0
elif dv==10:
  dv="k"  
  
print("dv=",dv)