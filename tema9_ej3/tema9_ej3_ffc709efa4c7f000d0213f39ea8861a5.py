def decodificar(mensaje):
    ##
    a = str(mensaje[0:8])
    d1=(int(str(a), 2))
    l1=chr(d1)
    ##
    b = str(mensaje[10:17])
    d2=(int(str(b), 2))
    l2=chr(d2)
    ##
    c = str(mensaje[19:26])
    d3=(int(str(c), 2))
    l3=chr(d3)
    ##
    d = str(mensaje[28:35])
    d4=(int(str(d), 2))
    l4=chr(d4)
    palabra = l1+l2+l3+l4
    return palabra
if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)