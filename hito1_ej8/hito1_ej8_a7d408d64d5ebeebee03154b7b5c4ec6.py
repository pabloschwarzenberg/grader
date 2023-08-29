Pp=int(input("Insertar numero de hasta 4 dígitos: "))
p=str(Pp)

if len(p)==4:
    a=p[0]
    x=p[1]
    y=p[2]
    z=p[3]
    if (a,x,y,z)!=0:
        print(a,"M +",x,"C +",y,"D +",z,"U")
elif len(p)==3:
    a=p[0]
    x=p[1]
    y=p[2]
    if(a,x,y)!=0:
        print(a,"C +",x,"D +",y,"U")
elif len(p)==2:
    a=p[0]
    x=p[1]
    if(a,x)!=0:
        print(a,"D +",x,"U")
elif len(p)==1:
    a=p[0]
    print(a,"U")