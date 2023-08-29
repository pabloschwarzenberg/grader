def numero_perfecto(a):
	count=1
	divisores=[]
	while count<a:
		if a%count==0:
			divisores.append(count)
		count+=1
	if sum(divisores)==a:
		return True
	else:
		return False