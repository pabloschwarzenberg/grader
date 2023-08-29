def decodificar(mensaje):
    lista_mensaje=mensaje.split(",")
    l=0
    mensaje_final=[]
    while l<len(lista_mensaje):
        i=0
        mensaje_semifinal=0
        while i<len(lista_mensaje[l]):
            potencia=2**(len(lista_mensaje[l])-i-1)
            mensaje_semifinal=mensaje_semifinal+(int(lista_mensaje[l][i])*potencia)
            i+=1
        mensaje_final.append(chr(mensaje_semifinal))
        l+=1
    mensaje_final="".join(mensaje_final)
    return mensaje_final

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)