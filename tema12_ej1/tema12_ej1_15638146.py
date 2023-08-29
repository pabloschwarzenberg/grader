def funcion(n,string=""):
	numeros=[0,1]
	if len(string)==n:
		print(string)
	else:
		for i in numeros:
			funcion(n,string+str(i))
		return ""
n=int(input("Ingrese el numero:"))
print(funcion(n,string=""))