num = input("Ingrese un numero de hasta 4 digitos: ")

magnitudes = [ "U", "D", "C", "M" ]
mag = []

out = ""

while (num[0] == "0"):
	num = num[1:]
	
for i in range(len(num)):
	mag.append(magnitudes[i])

magnitudes = list(reversed(mag))

for i in range(len(num)):
		if i == len(num)-1:
			out = out + num[i] + magnitudes[i]
		else:
			out = out + num[i] + magnitudes[i] + "+"
			
			
print(out)