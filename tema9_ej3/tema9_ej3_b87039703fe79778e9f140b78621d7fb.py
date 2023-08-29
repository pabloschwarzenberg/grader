def decodificar(mensaje):
    m=[]
    mensaje=mensaje.split(",")
    for i in range(len(mensaje)):
        if mensaje[i]=="01101000":
            m.append("h")
        if mensaje[i]=="01101111":
            m.append("o")
        if mensaje[i]=="01101100":
            m.append("l")
        if mensaje[i]=="01100001":
            m.append("a")
        #asi contunuaria con todas las letras y no necesito el paso de transformacion desde binario a entero :)
    m="".join(m)
    return m
if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         