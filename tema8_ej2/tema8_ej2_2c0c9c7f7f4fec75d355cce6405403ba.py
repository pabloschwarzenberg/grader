def buscarTodas(string,b):
	i=0
	nueva=[]
	while i<len(string):
		if string[i]==b:
			nueva.append(str(i))
		i+=1
	nueva=" ".join(nueva)	
	return nueva