#Ingreso de datos:
num = int(input("Ingrese numero a descomponer: "))

#Def. de variables de salida y auxiliares
out = [ ]
divisor = 2


# Cada numero no-primo es producto de dos factores mas pequeños, por lo tanto se busca el menor divisor para asegurar de que este sea primo:
while (divisor <= num):
	#Si encuentra divisor, lo agrega a la lista de salida
	if (num%divisor == 0):
		out.append(divisor)
		num /= divisor
	# Si no es divisor, avanza al siguiente numero y repite el proceso
	else:
		divisor += 1
		
for i in out:
			print(i)
			