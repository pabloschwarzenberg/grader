#Contestador de celular
ntelefono=str(eval(input("Ingrese numero de telefono de 8 digitos:")))
hdellamada=eval(input("Ingrese hora de llamada (ej: 23 o 7 o 0):"))
tresultdig=int(ntelefono[-3:])
tresprimdig=int(ntelefono[:3])
if(hdellamada>=0 and hdellamada<=7):
    print("CONTESTAR")
if(tresultdig==909 and hdellamada<=14):
    print("CONTESTAR")
if(hdellamada>=17 and hdellamada<=19 and tresprimdig<=876 and tresprimdig>=878):
    print("CONTESTAR")
else:
    ("NO CONTESTAR")
if(hdellamada>19):
    print("NO CONTESTAR")
if(tresprimdig==877):
    print("NO CONTESTAR")