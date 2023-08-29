#Contestador de celular
telefono=input("ingrese el número de telefono:")
hora=int(input("ingrese la hora:"))


if hora>=0 and hora>=7:
    print("contestar")

if hora<14 and telefono[-1]=="9" and telefono[-2]=="0" and telefono[-3]=="9":
    print("contestar")

if hora>=17 and hora<19:
    if telefono[0]=="8" and telefono[1]=="7" and telefono[2]=="7": 
        print("No Contestar")
    else:
        print("Contestar")
if hora>19:
    print("No contestar")      