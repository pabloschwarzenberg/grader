# completa el código de la función
def suma_divisores(a):
	count=1
	divisores=[]
	while count<a:
		if a%count==0:
			divisores.append(count)
		count+=1
	if sum(divisores)==1:
		return ((sum(divisores)),True)
	else:
		return ((sum(divisores)),False)