#Pedir los 4 números al usuario

numero = int(input("Ingrese un digito de 4 cifras: "))
largo = len(str(numero))
if largo == 4:
    n1 = numero // 1000
    n2 = (numero // 100) % 10
    n3 = (numero // 10) % 10
    n4 = numero % 10
    print(n1,n2,n3,n4)
    print(str(n1)+"M"+"+"+str(n2)+"C"+"+"+str(n3)+"D"+"+"+str(n4)+"U")
else:
    if largo == 3:
        n2 = (numero // 100) % 10
        n3 = (numero // 10) % 10
        n4 = numero % 10
        print(str(n2)+"C"+"+"+str(n3)+"D"+"+"+str(n4)+"U")
    else:
        if largo == 2:
            n3 = (numero // 10) % 10
            n4 = numero % 10
            print(str(n3)+"D"+"+"+str(n4)+"U")
        else:
            if largo == 1:
                print(str(numero)+"U")   