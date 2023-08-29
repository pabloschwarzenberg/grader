x=input("Ingrese la secuencia de gonoma: ")
z=[]
y=len(x)
for f in x:
	if f=="A" or f=="a" or f=="C" or f=="c" or f=="T" or f=="t" or f=="G" or f=="g":
		z.append(f)
d=len(z)
if y==d:
	print("La secuencia correcta")
else:
	print("Secuencia incorrecta")      