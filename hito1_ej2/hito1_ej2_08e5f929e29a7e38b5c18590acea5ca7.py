numero = int(input("ingrese el numero de telefono: "))
hora = int(input("ingrese la hora de la llamada: "))
numtrun = numero%1000
print(numtrun)
if hora>=0 and hora<=7:
    print("contestar")
if hora>=8 and hora<13:
    print("contestar")
if hora<14 and numtrun==909:
    print("contestar")
else:
    print("no contestar")
if hora>=14 and hora==15 and hora==16:
    print("contestar")
if hora==17 or hora==18 or hora==19 and numtrun==877:
    print("no contestar")
if hora==17 or hora==18 or hora==19 and numtrun>877 and numtrun<877:
    print("contestar")
if hora>=19 and hora<=0:
    print("no contestar")