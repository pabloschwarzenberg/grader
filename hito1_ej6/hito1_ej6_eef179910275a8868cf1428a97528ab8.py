#Ordenar tres números
x1=eval(input("ingrese el primer numero: "))
x2=eval(input("ingrese el segundo numero: "))
x3=eval(input("ingrese el tercer numero: "))
if x1>x2:
    if x1>x3:
        if x2>x3:
            print(str(x3)+","+str(x2)+","+str(x1))
        else:
            print(str(x2)+","+str(x3)+","+str(x1))
    else:
        print(str(x2)+","+str(x1)+","+str(x3))
else:
    if x1>x3:
        print(str(x3)+","+str(x1)+","+str(x2))
    else:
        if x2>x3:
            if x1>x3:
                print(str(x3)+","+str(x2)+","+str(x2))
            else:
                print(str(x1)+","+str(x3)+","+ str(x2))
        else:
            print(str(x1)+","+str(x2)+","+str(x3))