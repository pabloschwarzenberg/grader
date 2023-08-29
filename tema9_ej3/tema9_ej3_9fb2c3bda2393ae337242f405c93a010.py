def decodificar(mensaje):
    l=mensaje.split(",")
    lnum=[]
    for i in range(len(l)):
        num=0
        j=len(l[i])-1
        while j>=0:
            num+=int(l[i][j])*(2**int(len(l[i])-1-j))
            j+=-1
        lnum.append(num)
    letras=[]
    for num in lnum:
        letra=chr(num)
        letras.append(letra)
    mensaje=""
    for letra in letras:
        mensaje+=letra
    return mensaje

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         