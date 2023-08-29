#Elecciones
#Variables comuanles anales
votos_totales_comuna1 = int
votos_totales_comuna2 = int
votos_totales_comuna3 = int
votos_Isabel_comuna1 = int
votos_Isabel_comuna2 = int
votos_Isabel_comuna3 = int
operacion1 = int
operacion2 = int
operacion3 = int
x1 = ((operacion1*80/100))
x2 = ((operacion2*70/100))
x3 = ((operacion3*40/100))

#Ingresación Datal
votos_totales_comuna1 = int(input("Ingrese los votos totales de la comuna Minecraft: "))
votos_totales_comuna2 = int(input("Ingrese los votos totales de la comuna Half-Life: "))
votos_totales_comuna3 = int(input("Ingrese los votos totales de la comuna Assassin´s Creed: "))
votos_Isabel_comuna1 = int(input("Ingrese los votos por Isabela de la comuna Minecraft: "))
votos_Isabel_comuna2 = int(input("Ingrese los votos por Isabela de la comuna Half-Life: "))
votos_Isabel_comuna3 = int(input("Ingrese los votos por Isabela de la comuna Assassin´s Creed: "))

#Calculación Votal
if votos_totales_comuna1 > votos_Isabel_comuna1:
    operacion1 = ((votos_Isabel_comuna1*100)/votos_totales_comuna1)
print ("El porcentaje de votos por Isabela en Minecraft es: ", operacion1)

if votos_totales_comuna2 > votos_Isabel_comuna2:
    operacion2 = ((votos_Isabel_comuna2*100)/votos_totales_comuna2)
print ("El porcentaje de votos por Isabela en Half-Life es: ", operacion2)

if votos_totales_comuna3 > votos_Isabel_comuna3:
    operacion3 = ((votos_Isabel_comuna3*100)/votos_totales_comuna3)
print ("El porcentaje de votos por Isabela en Assassin´s Creed es: ", operacion3)

#Definir Ganación Caso 1
if operacion1 >= (operacion1*80/100)
  print ("Isabel es la ganadora, barvo !!111!!!")
else:
  print ("Calculando")
if operacion2 >= (operacion2*80/100)
else:
    print ("Calculando")
if operacion3 >= (operacion3*40)/100)
else:
    print ("Calculando")
    
#Definir Ganación Caso 2
if operacion1, operacion2 >= ((operacion1+operacion2)*70)/100
  print ("Isabel es la ganadora")
