#Contestador de celular
telefono= str(input("ingresar numero telefonico:"))
hora= int(input("ingresar la hora de la llamada:"))
if hora>=0  and hora<=7:
    print("contestar la llamada")
if hora >19 and hora<=23:
        print("no contestar")
else:
    if hora > 7 and hora <14 and str(telefono[-3]) =="9" and str(telefono[-2])=="0" and str(telefono[-1])=="9":
        print("contestar la llamada")
    if hora > 7 and hora <14 and str(telefono[-3]) !="9" and str(telefono[-2])!="0" and str(telefono[-1])!="9":
        print("no contestar")
    if hora > 17 and hora <19 and str(telefono[0:1]) =="8" and str(telefono[1:2])=="7" and str(telefono[2:3])=="7":
        print("no contestar")
    if hora > 17 and hora <19 and str(telefono[0:1]) !="8" and str(telefono[1:2])!="7" and str(telefono[2:3])!="7":
        print("contestar la llamada")        