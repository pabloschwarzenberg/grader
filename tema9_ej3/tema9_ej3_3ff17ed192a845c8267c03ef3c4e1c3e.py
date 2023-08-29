def decodificar(mensaje):
    num = mensaje.split(",")
    mensaje = ""
    for num_bin in num:
        num_dec = int(num_bin, 2)
        letra = chr(num_dec)
        mensaje += letra
    return mensaje

mensaje = decodificar("01101000,01101111,01101100,01100001")
print(mensaje)

         