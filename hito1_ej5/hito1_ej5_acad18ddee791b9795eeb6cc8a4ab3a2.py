#Cálculo del dígito verificador de un rut
r=(input("Ingrese RUT sin dijito verificador:"))
if(int(len(r))==8):
    a=(int(r[-1]))*2
    b=(int(r[-2]))*3
    c=(int(r[-3]))*4
    d=(int(r[-4]))*5
    e=(int(r[-5]))*6
    f=(int(r[-6]))*7
    g=(int(r[-7]))*2
    h=(int(r[-8]))*3
    x=(a+b+c+d+e+f+g+h)
    j=(x%11)
    t=(11-j)
    if(t==10):print("dv=k")
    else:
        if(t==11):print("dv=0")
        else: print ("dv="+str(t))
else:
    un=(int(r[-1]))*2
    do=(int(r[-2]))*3
    tr=(int(r[-3]))*4
    cu=(int(r[-4]))*5
    ci=(int(r[-5]))*6
    se=(int(r[-6]))*7
    si=(int(r[-7]))*2
    s=(un+do+tr+cu+ci+se+si)
    jw=(s%11)
    tu=(11-jw)
    if(tu==10):print("dv=k")
    else:
        if(tu==11):print("dv=0")
        else: print ("dv="+str(tu))
    
