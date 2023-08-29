# por favor escribe aquí tu función 
#def es_primo(numero):
# return 
def es_primo(numero):
    if numero == 0 or numero == 1 or numero == 4:
        return False
    for x in range(2, int(numero/2)):
        if numero % x == 0:
            return False
    return True
# Vamos desde el 1 hasta el 1000 (puse 1001 porque el límite no es inclusivo)
print("""
Imprimiendo números primos desde 1 hasta 1000
	https://parzibyte.me/blog 
""")
for numero in range(1001):
	if es_primo(numero):
		print(numero, end=",")