#Contestador de celular
numerodetelefono= input("su numero de telefono: ")
ultimosdijitos= numerodetelefono[5:8]
horadelllamado= int(input("hora de la llamada: "))
prinerosdigitos= numerodetelefono[0:3]

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
        print("CONTESTAR")
elif(horadelllamado>=19):
    print("NO CONTESTAR")      