def decodificar(mensaje):
    x=mensaje
    z=x.split(",")
    c="".join(z)
    n = int(c,2)
    k= n.to_bytes((n.bit_length() + 7) // 8, 'big').decode()
    return k      