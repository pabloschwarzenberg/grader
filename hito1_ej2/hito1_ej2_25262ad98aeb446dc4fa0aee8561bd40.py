#Contestador de celular

#Pedir datos:
num = input("Ingrese numero telefonico: ")
hora = int(input("Ingrese hora de la llamada: "))

out = "NO CONTESTAR"

if (hora >= 0) and (hora <= 7):
	out = "CONTESTAR"
	
elif (hora < 14):
	if num[-3:] == "909":
		out = "CONTESTAR"
	else:
		out = "NO CONTESTAR"
		
elif (hora >= 17) and (hora <= 19):
	if num[0:3] == "877":
		out = "NO CONTESTAR"
	else:
		out = "CONTESTAR"

else:
	out = "NO CONTESTAR"

print(out)