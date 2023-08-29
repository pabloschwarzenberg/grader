def decodificar(mensaje):
    md = ""
    cb = "" 
    for c in mensaje: 
        if c != ",":
            cb += c
        else: 
            ord_c = int(cb,2)
            md += chr(ord_c)
            cb = ""
    ord_c = int(cb,2)
    md += chr(ord_c)
    return md






