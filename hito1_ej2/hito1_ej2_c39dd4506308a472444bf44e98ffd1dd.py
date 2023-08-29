#Contestador de celular
print("ingrese telefono:")
telefono=int(input())
print("ingrese hora:")
hora=int(input())
if 0<hora<7:
    print("CONTESTAR")
elif 7<hora<14:
    if telefono%1000==909:
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
elif 14<hora<19:
    if telefono//100000==877:
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")
elif 19<hora<24:
    print("NO CONTESTAR")
     