#tu programa recibirá como parámetro un número que indicará el largo de las combinaciones de números binarios
#que se deben generar
n=int(input())
def funcion(n,string=""):
	numeros=[0,1]
	if len(string)==n:
		print(string)
	else:
		
		for i in numeros:
			funcion(n,string+str(i))
		return
funcion(n)