#Cálculo del dígito verificador de un rut
rut=input("ingrese numero de rut")
multiplo=2
n=len(rut)-1
suma=0

while n >=0:
    suma= suma + (int(rut[n])*multiplo)
    multiplo=multiplo+1
    if multiplo == 8:
       multiplo = 2
    n=n-1
resto= suma% 11
dv=11-resto
if dv==11:
   dv=0
elif dv==10:
   dv="k"
print("dv=", dv)