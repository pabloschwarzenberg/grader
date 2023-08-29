#Contestador de celular
número=int(input("Ingrese un número: "))
hora=int(input("Ingrese una hora: "))
if 0<=hora<=7:
    print("Resultado: Contestar")
if 7<hora<14:
    if número%1000==909:
        print("Resultado: Contestar")
    else:
        print("Resultado: No contestar")
if 14<=hora<=19:
    if 14<=hora<17:
        print("Resultado: No contestar")
    else:
        if 87699999<número<87800000:
            print("Resultado: No contestar")
        else:
            print("Resultado: Contestar")
if 19<hora:
    print("Resultado: No contestar")
