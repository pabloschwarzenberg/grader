#Contestador de celular
contacto = []
num = int(input("ingrese numero telefonico: "))
hora = int(input("Ingrese hora de la llamada: "))
contacto.append(num)
#print(contacto)
Ext = str(contacto[-1])
#print(Ext)
Var= int(Ext[-3:])
#print (Var)
#print(type (Var))

if Var == 909 and hora > 7 and hora < 14:
    print ("CONTESTAR")
else:
    if Var != 909 and hora > 7 and hora < 14:
        print("NO CONTESTAR")

if Var == 877 and hora > 17 and hora < 19:
    print ("CONTESTAR")
else:
    if Var != 877 and hora <= 19 and hora >= 17:
        print("NO CONTESTAR")

if hora >23 and hora <7:
    print("CONTESTAR")

if hora>19 and hora <= 23:
    print("NO CONTESTAR")