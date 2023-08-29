sec_adn = input("Ingrese secuencia de genoma: ")
validar = []
x = len(sec_adn)
for i in sec_adn:
	if i == "A" or i == "a" or i == "Y" or i == "y" or i == "X" or i == "x" or i == "G" or i == "g":
		validar.append(i)
y = len(validar)
if x == y:
	print("La secuencia correcta")
else:
	print("Secuencia incorrecta")