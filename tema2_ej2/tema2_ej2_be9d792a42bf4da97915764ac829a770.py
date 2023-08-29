# completa el código de la función
def amigos(a,b):
	num = a
	s=0
	for div in range(1,num+1):
		if (num % div) == 0 :
			if num != div:
				s = s + div
	if s == b:
		return True
	else:
		return False

           