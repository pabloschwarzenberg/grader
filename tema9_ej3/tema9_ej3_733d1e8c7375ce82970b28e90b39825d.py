def decodificar(mensaje):
    #separar codigos del mensaje en una lista
    mensaje=mensaje.split(",")
    #invertir codigos y agregar a lista nueva
    codigos_invertidos=[]
    x=0
    for codigo in mensaje:
        invertir=mensaje[x][::-1]
        codigos_invertidos.append(invertir)
        x+=1
    #convertir a decimal
    decimales=[]
    for codigo in codigos_invertidos:
        x=0
        sumar=0
        for i in codigo:
            calculo=int(i)*(2**x)
            sumar+=calculo
            x+=1
        decimales.append(sumar)
    #desifrar
    mensaje_desifrado=""
    for valor in decimales:
        letra=chr(valor)
        mensaje_desifrado+=letra      
    return mensaje_desifrado
          
if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)