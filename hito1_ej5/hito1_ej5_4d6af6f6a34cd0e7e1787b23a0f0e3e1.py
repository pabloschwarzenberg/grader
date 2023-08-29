#Cálculo del dígito verificador de un rut
rut=input("Ingrese R.U.T:")
rut=str(rut)
m=2
suma=0

for i in rut[::-1]:
    d=int(i)*m
    m=m+1

    suma=suma+d
    if m==8:
        m=2
    

r=suma%11

if r==0:
    print("dv=0")

else:
    digito=11-r


    if digito!=10:
       print("dv=",digito)

    elif digito==10:
        print("dv=k") 