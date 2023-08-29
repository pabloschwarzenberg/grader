def decodificar(mensaje):
    mensaje = mensaje.split(",")
    m_list = []
    hex_list = []
    for x in mensaje:
        m_list.append(int(x, 2))
    for n in m_list:
        hex_list.append(chr(n))
    hexadecimal = "".join( x for x in hex_list)
    return hexadecimal

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         