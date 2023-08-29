def convertir_binario_decimal(letra):
    I=7
    resultado=0
    while I>=0:
        exponente=7-I
        numero=int(letra[I])*(2**exponente)
        resultado=resultado+numero
        I=I-1
    return resultado 

def decodificar(mensaje):
    letras=mensaje.split(',')
    I=0
    resultado=""
    while I<len(letras):
        codigo=convertir_binario_decimal(letras[I])
        letra=chr(codigo)
        resultado=resultado+letra
        I=I+1
    return resultado 


mensaje=decodificar("01101000,01101111,01101100,01100001")
print(mensaje)
         