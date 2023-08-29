#Cálculo del dígito verificador de un rut
RUT=input("Ingrese su Rut sin puntos ni digito verificador: ")
s=0
m=2
for r in RUT [::-1]:
    s+=int(r)*m
    m+=1
    if m==8:
        m=2
r=s%11
resta=11-r
if resta==11:
    print("dv=0")
elif resta==10:
    print("dv=K")
else:
    print("dv=%d" %(resta))    