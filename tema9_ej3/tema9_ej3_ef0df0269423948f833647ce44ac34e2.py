def decodificar(mensaje):
    mensajes_real = ""
    decimales = []
    binarios = mensaje.split (",")
    
    for numero_binario in binarios: 
	    posicion = 0
	    decimal = 0
	    binario = numero_binario[::-1]
	    for digito in binario:
	        multiplicador = 2**posicion
	        decimal += int(digito) * multiplicador
	        posicion += 1 
	    decimales.append (decimal)
    
    
    for numero_decimal in decimales:
        mensajes_real = mensajes_real + chr(int(numero_decimal))
       
    return mensajes_real

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         