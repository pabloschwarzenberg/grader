def buscarTodas(a,b):
    cont_pos = -1
    final = ""
    for l in a:
        cont_pos += 1
        if l == b:
            pos = cont_pos
            rt = str(pos)
            v = final+rt
            final = v
            g = final+" "
            final = g
    f = final[:-1]
    final = f
    return final

           