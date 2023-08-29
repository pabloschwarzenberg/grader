def decodificar(mensaje):
    texto=[]
    mensaje=mensaje.split(',')
    for binario in mensaje:
        x=len(binario)-1
        num=0
        
        for numeros in binario:
            if numeros=='0':
                numero = 0
            else:
                numero=1
            b=numero*(2**x)
            num=num + b
            x=x-1
        texto.append(chr(num))
    texto=''.join(texto)
    return texto

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         