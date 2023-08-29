
def decodificar(mensaje):
    msglist = mensaje.split(",")
    out_str = ""
    for byte in msglist:
        dec = int(byte,2)
        c = chr(dec)
        out_str += c
    return out_str

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         