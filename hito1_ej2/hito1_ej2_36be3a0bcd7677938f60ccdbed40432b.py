#Contestador de celular
numeroCelular = int(input("ingrese numero telefonico: "))
hora = int(input("ingrese hora de la llamada: "))
terminado909 = numeroCelular - 909
variableContestar = 00 <= hora <= 7 or (17 <= hora <= 19
and 87700000 >= numeroCelular >= 87799999) or (8 <= hora <= 14 and terminado909%1000 == 0)

if variableContestar:
    print("CONTESTAR")
else:
    print("NO CONTESTAR")      