#Contestador de celular
numeroTelefonico=int(input("Ingrese numero telefonico:"))
hora=int(input("Ingrese hora de la llamada:"))
primerosNumeros=numeroTelefonico//100000
ultimosNumeros=numeroTelefonico%1000
contestar=False
if hora>=0 and hora<=7:
    contestar=True
elif hora<14 and ultimosNumeros==909:
    contestar=True
elif hora>=17 and hora<19 and primerosNumeros!=877:
    contestar=True
if contestar==True:
    resultado="CONTESTAR"
else:
    resultado="NO CONTESTAR"
print("Resultado:",resultado)       