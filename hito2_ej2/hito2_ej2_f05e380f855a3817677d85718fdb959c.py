secuencia=input("Ingrese la secuencia de gonoma: ")
comprobacion=[]
x=len(secuencia)
for i in secuencia:
	if i=="A" or i=="a" or i=="C" or i=="c" or i=="T" or i=="t" or i=="G" or i=="g":
		comprobacion.append(i)
c=len(comprobacion)
if x==c:
	print("La secuencia correcta")
else:
	print("Secuencia incorrecta")