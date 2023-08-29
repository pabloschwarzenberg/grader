#Cálculo del dígito verificador de un rut
#Entrada
rut=int(input("Ingrese rut: "))
#transformar a string
run=str(rut)

#separar rut 8 digitos
if  len(run)==8:
    a1=int(run[7])
    a2=int(run[6])
    a3=int(run[5])
    a4=int(run[4])
    a5=int(run[3])
    a6=int(run[2])
    a7=int(run[1])
    a8=int(run[0])
#cálculo dígito verificador
    suma1=(a1*2)+(a2*3)+(a3*4)+(a4*5)+(a5*6)+(a6*7)+(a7*2)+(a8*3)
    div1=(suma1//11)
    resto1=suma1-(div1*11)
    n1=11-resto1
    if  n1==11:
        print("dv=0")
    elif    n1==10:
        print("dv=K")
    else:
        print("dv="+str(n1))

#separar rut 7 digitos
elif  len(run)==7:
    b1=int(run[6])
    b2=int(run[5])
    b3=int(run[4])
    b4=int(run[3])
    b5=int(run[2])
    b6=int(run[1])
    b7=int(run[0])
#cálculo dígito verificador
    suma2=(b1*2)+(b2*3)+(b3*4)+(b4*5)+(b5*6)+(b6*7)+(b7*2)
    div2=(suma2//11)
    resto2=suma2-(div2*11)
    n2=11-resto2
    if  n2==11:
        print("dv=0")
    elif    n2==10:
        print("dv=K")
    else:
        print("dv="+str(n2))
else:
    print("rut invalido.")