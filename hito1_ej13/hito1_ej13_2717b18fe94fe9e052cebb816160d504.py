#Factores Primos

def es_primo(num):
	if(num > 1):
		for i in range(2, int(num * 0.5) + 1):
			if(num % i == 0):
				return False
	else:
		return False
	return True
def prime_facts(num):
	listprm=[]
	listdiv=[]
	if(num > 1):
		if(num == 2):
			listprm.append(2)

		for i in range(2, int(num * 0.5) + 1):
			i_int=int(i)
			if(es_primo(i_int) and num % i_int == 0):
				listprm.append(i_int)

		for j in range(1, num + 1):
			j_int=int(j)
			if(num % j_int == 0):
				listdiv.append(j)
		listdef = list(listdiv and listprm)

	else:
		pass
	
	return listdef

n=int(input("Ingrese un número: "))
x=prime_facts(n)
for i in x:
	print(i)