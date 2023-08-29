#Cálculo del dígito verificador de un rut
rut=input()
if len(rut)==8:
    primer_dig = rut[0]
    segund_dig = rut[1]
    tercer_dig = rut[2]
    cuarto_dig = rut[3]
    quint_dig = rut[4]
    sexto_dig = rut[5]
    sept_dig = rut[6]
    oct_dig = rut[7]

    a=int(oct_dig)*2
    b=int(sept_dig)*3
    c=int(sexto_dig)*4
    d=int(quint_dig)*5
    e=int(cuarto_dig)*6
    f=int(tercer_dig)*7
    g=int(segund_dig)*2
    h=int(primer_dig)*3

    n=a+b+c+d+e+f+g+h
else:
    
    primer_dig = rut[0]
    segund_dig = rut[1]
    tercer_dig = rut[2]
    cuarto_dig = rut[3]
    quint_dig = rut[4]
    sexto_dig = rut[5]
    sept_dig = rut[6]
    
    
    a=int(sept_dig)*2
    b=int(sexto_dig)*3
    c=int(quint_dig)*4
    d=int(cuarto_dig)*5
    e=int(tercer_dig)*6
    f=int(segund_dig)*7
    g=int(primer_dig)*2

    n=a+b+c+d+e+f+g

print("n "+str(n))
m=n//11
print("m=n//11 "+str(m))
t=n-(11*m)
print("t=n-(11*m) "+str(t))
v=11-t

if v==11:
    print("dv=0")
elif v==10:
    print("dv=K")
else:
    print("dv="+str(v))
         