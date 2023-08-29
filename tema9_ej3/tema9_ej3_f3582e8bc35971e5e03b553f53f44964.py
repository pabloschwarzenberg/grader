def decodificar(mensaje):
    lista=mensaje.split(",")
    i=0
    palabra=""
    while i<len(lista):
        if lista[i]=="01100001":
            palabra=palabra+"a"
        elif lista[i]=="01100010":
            palabra=palabra+"b"
        elif lista[i]=="01100011":
            palabra=palabra+"c"
        elif lista[i]=="01100100":
            palabra=palabra+"d"
        elif lista[i]=="01100101":
            palabra=palabra+"e"
        elif lista[i]=="01100110":
            palabra=palabra+"f"
        elif lista[i]=="01100111":
            palabra=palabra+"g"
        elif lista[i]=="01101000":
            palabra=palabra+"h"
        elif lista[i]=="01101001":
            palabra=palabra+"i"
        elif lista[i]=="01101010":
            palabra=palabra+"j"
        elif lista[i]=="01001011":
            palabra=palabra+"k"
        elif lista[i]=="01101100":
            palabra=palabra+"l"
        elif lista[i]=="01001101":
            palabra=palabra+"m"
        elif lista[i]=="01001110":
            palabra=palabra+"n"
        elif lista[i]=="01101111":
            palabra=palabra+"o"
        elif lista[i]=="00010000":
            palabra=palabra+"p"
        elif lista[i]=="00010001":
            palabra=palabra+"q"
        elif lista[i]=="00010010":
            palabra=palabra+"r"
        elif lista[i]=="00010011":
            palabra=palabra+"s"
        elif lista[i]=="00010100":
            palabra=palabra+"t"
        elif lista[i]=="00010101":
            palabra=palabra+"u"
        elif lista[i]=="00010110":
            palabra=palabra+"v"
        elif lista[i]=="00010111":
            palabra=palabbra+"w"
        elif lista[i]=="00011000":
            palabra=palabra+"x"
        elif lista[i]=="00011001":
            palabra=palabra+"y"
        elif lista[i]=="00011010":
            palabra=palabra+"z"
        i=i+1
    return palabra

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         