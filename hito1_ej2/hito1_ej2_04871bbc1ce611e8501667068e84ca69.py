#contestador automatico
print("numero telefonico de 8 digitos (numeros entre 0-23)")
numero= int(input("ingrese numero telefonico:"))
hora = int(input("ingrese la hora de la llamada:"))
resto = numero%1000
division_entera = numero//100000
if (hora >=0 and hora <=7):
    print("CONTESTAR")
elif (hora>=7 and hora < 14):
        if resto == 909:
            print("CONTESTAR")
        else:
            print("NO CONTESTAR")
elif (19 >= hora >= 17):
            if division_entera == 877:
                print("NO CONTESTAR")
            else:
                print("CONTESTAR")
elif (19 < hora < 23):
             print("NO CONTESTAR")
elif (hora==14):
     print("NO CONTESTAR")
