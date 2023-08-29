def numero_perfecto(a):
	s = []
	sDIVa = 0
	for i in range(a):
		if (a%(i+1) == 0):
			s.append(i+1)
	s.remove(a)
	for i in s:
		sDIVa += i
	print(s)
	print(sDIVa)
	if (sDIVa == a):
		return True
	else:
		return False
    
if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           