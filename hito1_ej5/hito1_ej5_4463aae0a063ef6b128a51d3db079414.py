#Cálculo del dígito verificador de un rut
rut=input("Ingrese un R.U.T. sin dígito verificador: ")
l=len(rut)
s=0
for i in range(l):
    j=l-i-1
    if(i%6==0):
        s+=int(rut[j])*2
    elif(i%6==1):
        s+=int(rut[j])*3
    elif(i%6==2):
        s+=int(rut[j])*4
    elif(i%6==3):
        s+=int(rut[j])*5
    elif(i%6==4):
        s+=int(rut[j])*6
    elif(i%6==5):
        s+=int(rut[j])*7
r=s%11
if(r==0):
    r=11
dv=11-r
if(dv==10):
    dv="k"
print("dv=",dv,sep="")