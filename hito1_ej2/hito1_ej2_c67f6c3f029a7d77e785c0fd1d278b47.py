numero=input()
numero1=int(numero)
telefono=str(numero1)
hora=input()
hora=int(hora)

if len(telefono)==8:
    if 0<=hora<=7:
        print("CONTESTAR")
    elif 7<hora<14 and telefono[5::]=="909":
        print("CONTESTAR")
    elif 7<hora<14 and telefono[5::]!="909":
        print("NO CONTESTAR")
    elif 17<=hora<=19 and telefono[0:3]!="877":
        print("CONTESTAR")
    elif 17<=hora<=19 and telefono[0:3]=="877":
        print("NO CONTESTAR")
    else:
        print("NO CONTESTAR")
else:
    print("numero ingresado incorrecto, intentelo denuevo")

