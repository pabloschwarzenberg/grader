def decodificar(mensaje):
    mensajeD=mensaje.split(",")
    codigo=[]
    mensajeN=""
    for x in range(len(mensajeD)):
        mensajeD2=mensajeD[x]
        mensajeD2=mensajeD2[::-1]
        digito=0
        for y in range(len(mensajeD2)):
            digito+=int(mensajeD2[y])*(2**y)
        codigo.append(chr(digito))
    for z in codigo:
        mensajeN+=str(z)
    mensaje=mensajeN
    return mensaje

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         