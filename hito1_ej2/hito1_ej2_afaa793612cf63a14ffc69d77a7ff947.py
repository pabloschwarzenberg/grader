#Contestador de celular
ntelefonico = int(input("ingrese numero telefonico:"))
hora = int(input("ingrese la hora de su llamada:"))

if (hora > 0 and hora < 7):
    print("CONTESTAR")

if (hora > 19):
    print("NO CONTESTAR")

if (hora < 14 and ntelefonico % 100000 == 909):
    print("CONTESTAR")

if (hora > 17 and hora < 19 or ntelefonico //10000 == 877):
    print("NO CONTESTAR")

else:
    print("CONTESTAR")      