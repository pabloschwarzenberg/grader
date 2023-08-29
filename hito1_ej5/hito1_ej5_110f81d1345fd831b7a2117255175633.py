#Cálculo del dígito verificador de un rut
enunciado = int(input("Infrese el RUT --> "))

numero=str(enunciado)

if len(str(enunciado))==8:
    uno=numero[7]
    dos=numero[6]
    tres=numero[5]
    cuatro=numero[4]
    cinco=numero[3]
    seis=numero[2]
    siete=numero[1]
    ocho=numero[0]

    s = int(uno)*2+int(dos)*3+int(tres)*4+int(cuatro)*5+int(cinco)*6+int(seis)*7+int(siete)*2+int(ocho)*3 
    a=s%11
    l=11-a

    if l==10:
        print("dv=K")

    if l==11:
        print("dv=0")

    if l<10:
        print("dv="+str(l))

if len(str(enunciado))==7:
    uno=numero[6]
    dos=numero[5]
    tres=numero[4]
    cuatro=numero[3]
    cinco=numero[2]
    seis=numero[1]
    siete=numero[0]

    s=int(uno)*2+int(dos)*3+int(tres)*4+int(cuatro)*5+int(cinco)*6+int(seis)*7+int(siete)*2
    a=s%11
    l=11-a

    if l==10:
        print("dv=K")

    if l==11:
        print("dv=0")

    if l<10:
        print("dv="+str(l))