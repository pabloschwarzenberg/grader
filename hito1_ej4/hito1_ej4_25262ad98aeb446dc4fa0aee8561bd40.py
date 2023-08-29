num = int(input("Ingresa un numero entero: "))

div = int(num)
resto = 0

out = ""

while True:
	if (div == 0) or (div == 1):
		break
	
	else:
		print(div)
	
		if (int(div%2) == 0):
			out = "0" + out
		else:
			out = "1" + out

		div = int(div / 2)

if (div == 1):
	out = "1" + out
else:
	out =  "0" + out

	
print("resultado="+out)