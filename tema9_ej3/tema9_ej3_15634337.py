__author__ = 'Domingo'
def decodificar(mensaje):
    lista_global=mensaje.split(',')
    lista_decimales=[]
    lista_ascii=[]
    for elemento in lista_global:
        elemento= [int(i) for i in elemento]
        lista_digitos=[]
        lista_terminos=[]
        for i in elemento:
            lista_digitos.append(i)
        lista_digitos.reverse()
        for i in range(len(lista_digitos)):
            num=lista_digitos[i]*(2**i)
            lista_terminos.append(num)
        suma=0
        for i in lista_terminos:
            suma=suma+i
        lista_decimales.append(suma)
    for i in lista_decimales:
        caracter=chr(i)
        lista_ascii.append(caracter)
    ans=''.join(lista_ascii)
    return ans

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         