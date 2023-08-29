#Contestador de celular
numero= eval(input("ingrese su numeor de celular de 8 digitos: "))
hora=int(input("ingrese la hora en la que llama entre 0 y 23: "))

numeroS=str(numero)
print(numeroS[5:8])


if hora >=0 and hora <=7:
    print("contestar")
elif hora>7 and hora <14:
    if numeroS[5:8]=="909":
        print("contestar")
    else:
        print("no contestar")
elif hora>= 14 and hora <17:
    print("no contestar")
elif hora>=17 and hora <=19:
    if numeroS[0:3]=="877":
        print("no contestar")
    else:
        print("contestar")
elif hora>19:
    print("no contestar")     