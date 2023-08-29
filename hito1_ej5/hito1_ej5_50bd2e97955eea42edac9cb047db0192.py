a=str(input("ingrese su rut:"))

A=eval (a)

if (A>=10000000):
    b = a[0:1]

    c = a[1:2]

    d = a[2:3]

    e= a[3:4]

    f= a[4:5]

    g= a[5:6]

    h= a[6:7]

    i = a[7:8]

    mb =eval (b)*3

    mc =eval (c)*2

    md =eval (d)*7

    me =eval (e)*6

    mf =eval (f)*5

    mg =eval (g)*4

    mh =eval (h)*3

    mi =eval (i)*2

    suma = mb+mc+md+me+mf+mg+mh+mi

    entera = suma//11

    noph = suma-(11*entera)

    vd = 11-noph
    
    if vd==10:
        print("dv=","K")

    elif vd==11:
        print("dv=","0")

    elif(vd != 10) or (vd!=11):
        print ("dv=",vd)

elif (A<9999999):
    b = a[0:1]

    c = a[1:2]

    d = a[2:3]

    e= a[3:4]
 
    f= a[4:5]

    g= a[5:6]

    h= a[6:7]

    mb =eval (b)*2

    mc =eval (c)*7

    md =eval (d)*6

    me =eval (e)*5

    mf =eval (f)*4

    mg =eval (g)*3

    mh =eval (h)*2

    suma = mb+mc+md+me+mf+mg+mh

    entera = suma//11

    noph = suma-(11*entera)

    vd = 11-noph

    if vd==10:
        print("dv=","K")

    elif vd==11:
        print("dv=","0")

    elif(vd != 10) or (vd!=11):
        print ("dv=",vd)

      

