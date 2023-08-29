telefono = int (input ("Ingrese numero telefono: "))
hora = int (input ("Ingrese hora de llamada: "))
tel = str(telefono)
prim = int (tel[:3])
ulti =int (tel[5:])
fijou = 909
fijop = 877
while not telefono >=10000000 and telefono <= 99999999:
    telefono = int (input ("Eoor Ingrese numero telefono de 8 digitos: "))

while not hora >=1 and hora <=23:
    hora = int (input ("Error Ingrese hora de llamada valida"))
   
if hora >=0 and hora <=7:
    print ("Contestar")
if hora >=19 and hora <=23:
    print ("no contestar")

if hora >=7 and hora <=14:
    if ulti == fijou:
        print ("contestar")
    else:
        print ("No contestar")
if hora >=17 and hora <=19:
    if prim == fijop:
        print ("No contestar")
    else:
        print ("Contestar")
