#Cálculo del dígito verificador de un rut
a=(input("RUT: "))
if len(a)==8:
    b=int(a[0])*8
    c=int(a[1])*9
    d=int(a[2])*4
    e=int(a[3])*5
    f=int(a[4])*6
    g=int(a[5])*7
    h=int(a[6])*8
    i=int(a[7])*9
    suma=int(b+c+d+e+f+g+h+i)
    resto=suma%11
    if resto==10:
        print("dv= k")
    print("dv= ", resto)
if len(a)==7:
    b=int(a[0])*9
    c=int(a[1])*4
    d=int(a[2])*5
    e=int(a[3])*6
    f=int(a[4])*7
    g=int(a[5])*8
    h=int(a[6])*9
    suma=int(b+c+d+e+f+g+h)
    resto=suma%11
    if resto==10:
        print("dv= k")
    print("dv= ", resto)   