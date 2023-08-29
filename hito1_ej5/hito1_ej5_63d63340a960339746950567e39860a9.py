#Cálculo del dígito verificador de un rut
numero = int(input("ingrese su rut sin verificador: "))
if numero<=99999999 and numero>=10000000:
    A=(numero%10)
    B=(numero//10)%10
    C=(numero//100)%10
    D=(numero//1000)%10
    E=(numero//10000)%10
    F=(numero//100000)%10
    G=(numero//1000000)%10
    H=(numero//10000000)%10
    
    A1=A*2
    B1=B*3
    C1=C*4
    D1=D*5
    E1=E*6
    F1=F*7
    G1=G*2
    H1=H*3

    suma=A1+B1+C1+D1+E1+F1+G1+H1
    modulo=suma//11
    resto1=suma-(11*modulo)
    
    resultado= 11-resto1
    if resultado==10:
        resultado="k"
        str(resultado)
        print("dv=",resultado)
    elif resultado==11:
        resultado="0"
        str(resultado)
        print("dv=",resultado)
    else:
        str(resultado)
        print("dv=",resultado)
elif numero<=9999999 and numero>=1000000:
    A=(numero%10)
    B=(numero//10)%10
    C=(numero//100)%10
    D=(numero//1000)%10
    E=(numero//10000)%10
    F=(numero//100000)%10
    G=(numero//1000000)%10
    
    A1=A*2
    B1=B*3
    C1=C*4
    D1=D*5
    E1=E*6
    F1=F*7
    G1=G*2

    suma=A1+B1+C1+D1+E1+F1+G1
    modulo=suma//11
    resto1=suma-(11*modulo)
    
    resultado= 11-resto1
    if resultado==10:
        resultado="k"
        str(resultado)
        print("dv=",resultado)
    elif resultado==11:
        resultado="0"
        str(resultado)
        print("dv=",resultado)
    else:
        str(resultado)
        print("dv=",resultado)