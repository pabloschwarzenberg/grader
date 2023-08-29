#Cálculo del dígito verificador de un rut
rut = str(input("ingrese su rut: "))
if(len(rut) == 8):
    n1 = rut[-1]
    n2 = rut[-2]
    n3 = rut[-3]
    n4 = rut[-4]
    n5 = rut[-5]
    n6 = rut[-6]
    n7 = rut[-7]
    n8 = rut[-8]
    suma =(int(n1)*2)+(int(n2)*3)+(int(n3)*4)+(int(n4)*5)+(int(n5)*6)+(int(n6)*7)+(int(n7)*2)+(int(n8)*3)
    resultado = 11-(suma-(11*int(suma/11)))
    if(resultado == 11):
        print("dv=0")
    elif(resultado == 10):
        print("dv=k")
    else:
        print("dv="+str(resultado))
elif(len(rut) == 7):
    n1 = rut[-1]
    n2 = rut[-2]
    n3 = rut[-3]
    n4 = rut[-4]
    n5 = rut[-5]
    n6 = rut[-6]
    n7 = rut[-7]
    suma =(int(n1)*2)+(int(n2)*3)+(int(n3)*4)+(int(n4)*5)+(int(n5)*6)+(int(n6)*7)+(int(n7)*2)
    resultado = 11-(suma-(11*int(suma/11)))
    if(resultado == 11):
        print("dv=0")
    elif(resultado == 10):
        print("dv=K")
    else:
        print("dv="+str(resultado))
else:
    print("syntax error")

