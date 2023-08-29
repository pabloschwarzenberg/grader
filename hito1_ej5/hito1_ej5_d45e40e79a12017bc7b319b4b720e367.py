


from itertools import count


ruta=  input("ingrese rut:     ")
rut=str(ruta)
cuenta1 = len(rut)
cuenta=int(cuenta1)
if cuenta ==8:
    a=int(rut[0])*3
    b=int(rut[1])*2
    c=int(rut[2])*7
    d=int(rut[3])*6
    e=int(rut[4])*5
    f=int(rut[5])*4
    g=int(rut[6])*3
    h=int(rut[7])*2
    suma=a+b+c+d+e+f+g+h
    i=int(suma/11)
    j=int(suma-(11*i))
    l=11-j
    if l ==11:
        print("dv= 0",)
    if l==10:
        print("dv= k")
    if l !=11 and l!=10:
        print("dv=",l)
if cuenta==7:
    a=int(rut[0])*2
    b=int(rut[1])*7
    c=int(rut[2])*6
    d=int(rut[3])*5
    e=int(rut[4])*4
    f=int(rut[5])*3
    g=int(rut[6])*2
    suma=a+b+c+d+e+f+g
    i=int(suma/11)
    j=int(suma-(11*i))
    l=11-j
    if l ==11:
        print("dv= 0",)
    if l==10:
        print("dv= k")
    if l !=11 and l!=10:
        print("dv=",l)
