def decodificar(mensaje):
    a=mensaje.split(",")
    string=[]
    for i in range(len(a)):
        a1=a[i]
        b=0
        numero=128
        for n in range(8):
            a2=a1[n]
            b+=int(a2)*int(numero)
            numero/=2
        string.append(chr(b))
    string="".join(string)
    return(string)

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
