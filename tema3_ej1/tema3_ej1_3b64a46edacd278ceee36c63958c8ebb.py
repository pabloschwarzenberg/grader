def suma_divisores(a):
	sa = []
	sDIVa = 0
	for i in range(a) :
		if(a%(i+1) == 0) :
			sa.append(i+1)
		i += 1
	sa.remove(a)
	for i in sa :
		sDIVa = sDIVa + i
	if(sDIVa == 1):
		return(sDIVa,True)
	else:
		return(sDIVa,False)