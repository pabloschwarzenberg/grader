llamada= int(input("Ingrese número telefónico: "))
hora_llamada= float(input("Ingrese hora de la llamada: "))
digitos= llamada%1000
primerdigi= int(str(llamada)[0:3])

if hora_llamada>=0 and hora_llamada<=7:
    print("CONTESTAR")
elif hora_llamada<14:
    if digitos==909:
        print("CONTESTAR")
    else:    
        print("NO CONTESTAR")
elif hora_llamada>=17 and hora_llamada<=19:
    if primerdigi==877:
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")
else:
    print("NO CONTESTAR")