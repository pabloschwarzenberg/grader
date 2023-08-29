def decodificar(mensaje):
    a=mensaje.replace("01101000","h")
    b=a.replace("01101111","o")
    c=b.replace("01101100","l")
    d=c.replace("01100001","a")
    mensaje=d.replace(",","")

    return mensaje

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         