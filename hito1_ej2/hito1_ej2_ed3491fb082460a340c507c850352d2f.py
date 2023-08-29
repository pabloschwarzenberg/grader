#Contestador de celular
numero = int(input("ingrese su numero telefonico")) #8
hora = int(input("ingrese la hora de llamada, entre las 0 y las 23 horas"))

if 0 < hora < 23:
    if 0 < hora < 7:
        print("CONTESTAR")
    elif hora < 14 and str(numero)[5]=="9" and str(numero)[6]=="0" and str(numero)[7]=="9":
        print("CONTESTAR")
    elif  17 < hora < 19 and str(numero)[0]!="8" and str(numero)[1]!="7" and str(numero)[2]!="7" :
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
         