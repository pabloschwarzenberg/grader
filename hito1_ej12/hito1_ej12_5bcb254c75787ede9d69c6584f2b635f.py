#Juego adivina mi número
def juego1():
	print ("Bienvenido")
	r=random.randrange(1,101) #hacemos que devuelva un valor a voleo entre el rango de 1 al 101
	numero_intentos=0
	while True: #bucle infinito
		print ("haga su intento")
		intento = input("?")
		if intento == r:
			break #rompemos el bucle cuando acierte el numero
		if intento > r:
			print ("Ingrese un numero mas chico")
		if intento < r:
			print ("Ingresee un numero mas grande")
		numero_intentos+=1
	print ("correcto")
	print (("numero de intentos"), numero_intentos)
 
juego1()      