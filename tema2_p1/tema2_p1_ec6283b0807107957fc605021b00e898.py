# por favor escribe aquí tu función
def primo(numero):
    if numero == 0 or numero == 1 or numero == 4:
        return False
    for x in range(2, int(numero/2)):
        if numero % x == 0:
            return False
    return True
numero = int(input("Ingrese su numero: "))
es_primo = primo(numero)
if es_primo:
	print("True")
else:
	print("False")