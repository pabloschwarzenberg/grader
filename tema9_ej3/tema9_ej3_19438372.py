def binario_decimal(binario):
    b=list(binario)
    b.reverse()
    resultado=0
    n=0
    for i in b:
        resultado+=int(i)*(2**n)
        n+=1
    return resultado



def decodificar(mensaje):
    b=mensaje.split(",")
    final=''
    for i in b:
        final+=chr(binario_decimal(i))
    return final

print(decodificar('01101000,01101111,01101100,01100001'))
        
        

