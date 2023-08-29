sec=input("Ingrese la secuencia de gonoma: ")
com=[]
t=len(sec)
for i in sec:
	if i=="A" or i=="a" or i=="C" or i=="c" or i=="T" or i=="t" or i=="G" or i=="g":
		com.append(i)
c=len(com)
if t==c:
	print("La secuencia es correcta")
else:
	print("Secuencia incorrecta")