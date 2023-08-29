import random

def ocultar_letras(palabra,cantidad):
	largo = len(palabra)
	while cantidad > 0:
		index_letras = random.randint(0, largo-1)
		if(palabra[index_letras] != "_"):
			palabra = palabra[:index_letras]+"_"+palabra[index_letras+1:]
			cantidad -= 1
	return palabra
def revisar_letra(palabra_secreta,palabra,letra):
	for l in range(len(palabra_secreta)):
		if(palabra_secreta[l] == letra and palabra[l] == "_"):
			palabra = palabra[:l]+palabra_secreta[l]+palabra[l+1:]
	return palabra


if __name__ == "__main__":
    words = ['lepidoptero', 'cantinflas', 'otorrinolaringologo']
    palabra_elegir = random.choice(words)
    palabra_modificado = ocultar_letras(palabra_elegir,3)
    while(palabra_elegir != palabra_modificado):
	    print(palabra_modificado)
	    x = input()
	    palabra_modificado = revisar_letra(palabra_elegir, palabra_modificado, x)
    print("{} -> {}".format(palabra_elegir, palabra_modificado))
