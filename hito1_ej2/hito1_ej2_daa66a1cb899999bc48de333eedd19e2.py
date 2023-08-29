#Contestador de celular
while True:
    numerodetelefono= input("su numero de telefono")
    numero = str(numerodetelefono)
    if(len(numero)==8):
        break
    else:
        print("vuelva a intentarlo")
while True:
    horadelllamado= int(input("hora de la llamada"))
    if(horadelllamado<=24 and horadelllamado>=0):
        break
    else:
        print("vuelva a intentarlo")
prinerosdigitos= numerodetelefono[0:3]
ultimosdijitos= numerodetelefono[5:8]
if(horadelllamado>=0 and horadelllamado<=7):
    print("CONTESTAR")
elif(horadelllamado<14):
    if(ultimosdijitos=="909"):
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
if(horadelllamado>17 and horadelllamado<19):
    if (prinerosdigitos == "877"):
        print("NO CONTESTAR")
    else:
        print("RESPONDER")
elif(horadelllamado>=19):
    print("NO CONTESTAR")      