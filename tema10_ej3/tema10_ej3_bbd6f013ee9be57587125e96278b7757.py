def sopaletras(nombre_archivo, palabras):
    t = []
    l_t = []
    p = []
    cont = 0
    archivo = open(nombre_archivo, "r")
    l = archivo.readlines()
    archivo.close()
    for i in l:
        l_t.append("".join(i.strip().split(" ")))
    x = 0
    y = 0
    for i in palabras:
        p.append(i.upper())
    i = 0
    for l1 in l_t:
        for l2 in p:
            if l2 in l1:
                t.append((palabras[i], [l1.index(l2),y],"derecha"))
            i += 1
        i = 0
        y += 1
    return t
if __name__ == "__main__":
  print sopaletras("sopa.txt",["casa"])