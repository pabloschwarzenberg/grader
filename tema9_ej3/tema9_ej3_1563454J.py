def decodificar(mensaje):
    import string
    mensaje=mensaje.split(',')
    mensajel=list(mensaje)
    mensaje=''
    for i in range (len(mensajel)):
        parte=mensajel[i]
        if parte[7]=='1':
            a=1
        elif parte[7]=='0':
            a=0
        if parte[6]=='1':
            b=2
        if parte[6]=='0':
            b=0
        if parte[5]=='1':
            c=4
        if parte[5]=='0':
            c=0
        if parte[4]=='1':
            d=8
        if parte[4]=='0':
            d=0
        if parte[3]=='1':
            e=16
        if parte[3]=='0':
            e=0
        if parte[2]=='1':
            f=32
        if parte[2]=='0':
            f=0
        if parte[1]=='1':
            g=64
        if parte[1]=='0':
            g=0
        decimal=a+b+c+d+e+f+g
        letras=string.ascii_lowercase
        decimal=decimal-97
        letra=letras[decimal]
        mensaje=mensaje+letra
    return mensaje

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         