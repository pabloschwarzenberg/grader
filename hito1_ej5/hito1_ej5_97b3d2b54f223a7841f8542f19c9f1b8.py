#Cálculo del dígito verificador de un rut
ingreso_sin_dv= int(input("Ingrese rut sin dv: "))
x=str(ingreso_sin_dv)

if len(x)==8:
    a=int(x[7])*2
    b=int(x[6])*3
    c=int(x[5])*4
    d=int(x[4])*5
    e=int(x[3])*6
    f=int(x[2])*7
    g=int(x[1])*2
    h=int(x[0])*3

    r= a+b+c+d+e+f+g+h
    p= int(r/11)
    q= r-(11*p)
    s= 11-q
    if s == 11:
        dv = 0
    if s == 10:
        dv = "k"
    print("dv="+dv)
else:

    b=int(x[6])*2
    c=int(x[5])*3
    d=int(x[4])*4
    e=int(x[3])*5
    f=int(x[2])*6
    g=int(x[1])*7
    h=int(x[0])*2

    r= b+c+d+e+f+g+h
    p= int(r/11)
    q= r-(11*p)
    s= 11-q
    dv= s
    if s == 11:
        dv = 0
    if s == 10:
        dv = "K"
    print("dv="+str(dv))