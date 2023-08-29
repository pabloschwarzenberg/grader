def jerigonzo(a):
	vocales=["a","e","i","o","u"]
	x=list(a)
	y=[]
	for i in range(len(a)):
		if str(x[i]) in vocales:   #Por que lo tuve que pasar a String?
			y.append(x[i]+"p"+x[i])
			#x[i]=x[i]+"p"+x[i]
		else:
			y.append(x[i])
	return "".join(y)
         