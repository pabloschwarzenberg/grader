rut = input("ingrese su rut: ")
A= len(rut)
if len(rut)==8:
    rut = list(rut)
    A=rut[7]
    A=int(A)*2
    B=rut[6]
    B=int(B)*3
    C=rut[5]
    C=int(C)*4
    D=rut[4]
    D=int(D)*5
    E=rut[3]
    E=int(E)*6
    F=rut[2]
    F=int(F)*7
    G=rut[1]
    G=int(G)*2
    H=rut[0]
    H=int(H)*3
    su=A+B+C+D+E+F+G+H
    dv=su%11
    resultado=11-dv
    if resultado == 11:
        resultado = 0
    if resultado == 10:
        resultado = str("k")
  
if len(rut)==7:
    rut = list(rut)
    A=rut[6]
    A=int(A)*2
    B=rut[5]
    B=int(B)*3
    C=rut[4]
    C=int(C)*4
    D=rut[3]
    D=int(D)*5
    E=rut[2]
    E=int(E)*6
    F=rut[1]
    F=int(F)*7
    G=rut[0]
    G=int(G)*2
    su=A+B+C+D+E+F+G
    dv =su%11
    resultado =11-dv
    if resultado == 11:
        resultado = 0
    if resultado == 10:
        resultado = str("k")
print("dv=", resultado)   