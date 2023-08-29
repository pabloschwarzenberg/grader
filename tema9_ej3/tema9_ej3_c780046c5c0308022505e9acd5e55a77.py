def decodificar(mensaje):
    mensaje=mensaje.split(',')
    mensaje_decodificado=''
    for binario in mensaje:
        numero=binario[::1]
        i=len(numero)-1
        valor=0
        for c in numero:
              valor+=(int(c)*(2**i))
              i-=1
        mensaje_decodificado=mensaje_decodificado+chr(valor)
    return mensaje_decodificado

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         