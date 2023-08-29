#1)
def buscarTodas(a,b):
	lista=[]
	for i in range(len(a)):
		if a[i]==b:
			lista.append(i)
	#return (lista)   #Transformar en string
	string=""
	for i in lista:
		string=string+str(i)+" "
	return string.strip()

#Esta bueno >:(