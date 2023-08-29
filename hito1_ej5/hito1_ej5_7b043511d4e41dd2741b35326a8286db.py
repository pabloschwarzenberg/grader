rut = str(input("Ingresa el rut para calcular el digito verificador: "))
if(len(rut) == 8):
    n1 = rut[-1]
    n2 = rut[-2]
    n3 = rut[-3]
    n4 = rut[-4]
    n5 = rut[-5]
    n6 = rut[-6]
    n7 = rut[-7]
    n8 = rut[-8]
    firstTotal = (int(n1)*2)+(int(n2)*3)+(int(n3)*4)+(int(n4)*5)+(int(n5)*6)+(int(n6)*7)+(int(n7)*2)+(int(n8)*3)
    result = 11-(firstTotal-(11*int(firstTotal/11)))
    if(result == 11):
        print("dv=0")
    elif(result == 10):
        print("dv=k")
    else:
        print("dv="+str(result))
elif(len(rut) == 7):
    n1 = rut[-1]
    n2 = rut[-2]
    n3 = rut[-3]
    n4 = rut[-4]
    n5 = rut[-5]
    n6 = rut[-6]
    n7 = rut[-7]
    firstTotal = (int(n1)*2)+(int(n2)*3)+(int(n3)*4)+(int(n4)*5)+(int(n5)*6)+(int(n6)*7)+(int(n7)*2)
    result = 11-(firstTotal-(11*int(firstTotal/11)))
    if(result == 11):
        print("dv=0")
    elif(result == 10):
        print("dv=K")
    else:
        print("dv="+str(result))
else:
    print("Invalido.")