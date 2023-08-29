import random
pss=["trampolin","perro","caballo"]
j=random.randint(0,2)
ps=pss[j]

def ocultar_letras(palabra,cantidad):
    import random
    global ps
    palabra = list(ps)
    i = 0
    while i < cantidad:
        palabra = list(palabra)
        slot = random.randint(0, len(palabra) - 1)
        if palabra[slot] == "_":
            continue
        palabra[slot] = "_"
        palabra = "".join(palabra)

        i += 1

    return palabra

def revisar_letra(ps,palabra,letra):
    if ps.find(letra) == -1:
       print("fallaste")
    else:
        h = 0
        while True:
            h = ps.find(letra, h)
            if h == -1:
                break
            palabra = list(palabra)
            palabra[h] = letra
            palabra = "".join(palabra)
            h += 1
    return palabra

