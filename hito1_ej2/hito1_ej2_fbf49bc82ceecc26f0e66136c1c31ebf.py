#Contestador de celular
numero = str(input("ingrese numero:"))
hora = int(input("hora:"))

ult3Num = int(numero[len(numero)-3:len(numero)])


#hora entre 7
if hora >= 0 and hora <= 7:
    print("CONTESTAR")
elif ult3Num == 909 and hora <= 14:
    print("CONTESTAR")
elif hora >=17 and hora <=19 and not ult3Num:
    print("CONTESTAR")
else:
    print("NO CONTESTAR")
    
