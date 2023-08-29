def binario_a_decimal(numero_binario):
	numero_decimal = 0 

	for posicion, digito_string in enumerate(numero_binario[::-1]):
		numero_decimal += int(digito_string) * 2 ** posicion

	return numero_decimal
def decodificar(mensaje):
    lista = mensaje.split(",")
    largo = len(lista)
    texto = ""
    
    i=0
    while  i < largo :

        
        numero = binario_a_decimal(lista[i])
        
        caracter = chr(numero)
        
        texto = texto + caracter
        
        i = i + 1

    return texto        