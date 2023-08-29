#Contestador de celular
numero=str(input("ingrese numero telefonico:"))
hora=int(input("Ingrese hora de la llamada:"))
if len(numero)==8:
    if hora>0 and hora<7:
        print("CONTESTAR")
    elif hora>7 and hora<14:
        if numero[-1]=="9"and numero[-2]=="0"and numero[-3]=="9":
            print("CONTESTAR")
        else:
            print("NO CONTESTAR")
    elif hora>17 and hora<19:
        if numero[0]=="8"and numero[1]=="7"and numero[2]=="7":
            print("NO CONTESTAR.")
        else:
            print("CONTESTAR")
    elif hora>19 and hora<24:
        print("NO CONTESTAR")
    else:
        print("hora no valida")
else:
    print("Numero no valido.")

