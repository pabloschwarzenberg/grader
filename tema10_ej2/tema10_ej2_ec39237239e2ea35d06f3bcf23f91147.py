#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales

palabra1='pelaos'
palabra2='pelao'
def levenshtein(palabra1,palabra2):
	diff = set(palabra1) ^ set(palabra2)
	t_diff = len(diff)
	long1=len(palabra1)
	long2=len(palabra2)
	x='0D'
	
	if t_diff == long1 or t_diff == long2:
		x='+1'
		return x
	else:
		if palabra1 != palabra2 and long1 == long2:
			x='1S'
			return x
		if palabra1 != palabra2 and long1+1 == long2 or long1 == long2+1:
			x='IB'
			return x
		if palabra1 != palabra2 and long1 != long2:
			x='+1'
			return x
		
		else:
			return x
resultado=levenshtein(palabra1,palabra2)
print(resultado)
if __name__=="__main__":
    pass
           