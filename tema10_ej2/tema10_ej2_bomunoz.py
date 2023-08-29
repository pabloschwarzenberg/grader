
def levenshtein(x,y):
	if x==y:
		return "0D"
	else:
		if len(x)==len(y):
			contador=0
			for i in range(len(x)):
				if x[i]!=y[i]:
					contador+=1
			if contador>1:
				return "+1"
			else:
				return "1S"

			
		else:
			z=list(y)
			for i in range(len(x)):
				if x[i] in z:
					z.remove(x[i])
			if len(z)>1:
				return "+1"
			else:
				return "IB"




			if abs(len(x)-len(y))==len(z):
				print ("Agregue/quite: ", len(z), "caracteres")
			else:
				print ("Operacion mixta")