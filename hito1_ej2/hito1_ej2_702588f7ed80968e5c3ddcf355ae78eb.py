#Contestador de celular
numero=input("numero de telefono: ", )
hora=int(input("hora: ", ))
if hora<8:
    print("contestar: ")
elif hora<14:
    if numero[5:8]=="909":
       print("contestar: ")
    else:
        print("no contestar: ")
elif hora>17 and hora<19:
    if numero[0:3]=="877":
        print("no contestar: ")
    else:
        print("contestar: ")
elif hora>19:
    print("no contestar: ")
    