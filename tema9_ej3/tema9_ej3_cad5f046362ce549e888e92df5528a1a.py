def decodificar(mensaje):
    md = ""
    cb = ""
    for c in mensaje:
        if c!=",":
            cb = cb + c
        else:
            ord_car = int(cb,2)
            md = md + chr(ord_car)
            cb = "" 
    ord_car = int(cb,2)
    md = md + chr(ord_car)
    return md
         