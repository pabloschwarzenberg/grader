#Cálculo del dígito verificador de un rut
rut=str(input())
x=len(rut)
N=rut
if x==8:
    a=int(N[7])*2
    b=int(N[6])*3
    c=int(N[5])*4
    d=int(N[4])*5
    e=int(N[3])*6
    f=int(N[2])*7
    g=int(N[1])*2
    h=int(N[0])*3
    suma=a+b+c+d+e+f+g+h
    resto=suma%11
    digito=11-resto
    
if x==7:
    a=int(N[6])*2
    b=int(N[5])*3
    c=int(N[4])*4
    d=int(N[3])*5
    e=int(N[2])*6
    f=int(N[1])*7
    g=int(N[0])*2
    suma=a+b+c+d+e+f+g
    resto=suma%11
    digito=11-resto

if digito==11:
    dv=0
elif digito==10:
    dv="k"
else:
    dv=digito

print("dv={}".format(dv))
      
