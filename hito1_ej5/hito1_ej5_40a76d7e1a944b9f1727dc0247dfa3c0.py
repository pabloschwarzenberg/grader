rut=int(input("ingrese su rut: "))
l=len(str(rut))
if l==8:
    a=int(str(rut)[7:8])
    b=int(str(rut)[6:7])
    c=int(str(rut)[5:6])
    d=int(str(rut)[4:5])
    e=int(str(rut)[3:4])
    f=int(str(rut)[2:3])
    g=int(str(rut)[1:2])
    h=int(str(rut)[0:1])

    procedimiento=(a*2)+(b*3)+(c*4)+(d*5)+(e*6)+(f*7)+(g*2)+(h*3)
else:
    b=int(str(rut)[6:7])
    c=int(str(rut)[5:6])
    d=int(str(rut)[4:5])
    e=int(str(rut)[3:4])
    f=int(str(rut)[2:3])
    g=int(str(rut)[1:2])
    h=int(str(rut)[0:1])

    procedimiento=(b*2)+(c*3)+(d*4)+(e*5)+(f*6)+(g*7)+(h*2)
    

divicion=procedimiento//11
resta=procedimiento-(11*divicion)
resultado=11-resta

if( resultado==11 ):
    print("dv=0")
elif( resultado==10 ):
    print("dv=K")
else:
    print("dv=",resultado)
