#Cálculo del dígito verificador de un rut
x=str(input("Ingrese rut: "))


if len(x)==7:
    a=x[6:]
    resto=x[:6]
    a=int(a)
    
    b=resto[5:]
    resto=resto[:5]
    b=int(b)

    c=resto[4:]
    resto=resto[:4]
    c=int(c)

    d=resto[3:]
    resto=resto[:3]
    d=int(d)

    e=resto[2:]
    resto=resto[:2]
    e=int(e)

    f=resto[1:]
    resto=resto[:1]
    f=int(f)

    g=x[:1]
    g=int(g)

    a1=a*2
    b1=b*3
    c1=c*4
    d1=d*5
    e1=e*6
    f1=f*7
    g1=g*2

    suma= a1+b1+c1+d1+e1+f1+g1
    entero=suma/11
    resto=suma%11
    digito=11-resto

    
if len(x)==8:
    a=x[7:]
    resto=x[:7]
    a=int(a)
    
    b=resto[6:]
    resto=resto[:6]
    b=int(b)

    c=resto[5:]
    resto=resto[:5]
    c=int(c)

    d=resto[4:]
    resto=resto[:4]
    d=int(d)

    e=resto[3:]
    resto=resto[:3]
    e=int(e)

    f=resto[2:]
    resto=resto[:2]
    f=int(f)

    g=resto[1:]
    resto=resto[:1]
    g=int(g)

    h=x[:1]
    h=int(h)

    a1=a*2
    b1=b*3
    c1=c*4
    d1=d*5
    e1=e*6
    f1=f*7
    g1=g*2
    h1=h*3

    suma= a1+b1+c1+d1+e1+f1+g1+h1
    entero=suma/11
    resto=suma%11
    digito=11-resto

if digito==11:
    print("dv= 0")
elif digito==10:
    print("dv= K")
else:
    print("dv=",digito)


