def decodificar(mensaje):
    
    lista=mensaje.split(",")
    numerosdecimales=[]
    for i in lista:
        numeroenbinario=list(i)
        numeroenbinario.reverse()

        suma=0
        i=0

        for cadadigito in numeroenbinario:
            potencia=int(cadadigito)*(2**(i))
            suma=suma+potencia
            i=i+1
        numerosdecimales.append(suma)
    listaletras=[]
    for cadadecimal in numerosdecimales:
        a=chr(cadadecimal)
        listaletras.append(a)

    s="".join(listaletras)
    return s
if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
        