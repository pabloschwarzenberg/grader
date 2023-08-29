#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(palabra1,palabra2):
    pass
def decodificar(m):
    m = m.split(",")
    p_c = []
    for i in m:
        ci = 0 
        e = 7
        for k in i:
            op = 2 ** e
            if k == "0":
                ci += 0
            else:
                ci += op
            e -= 1
        l = chr(ci)
        p_c.append(l)
        m = "".join(p_c)
    return m
if __name__=="__main__":
    pass
           