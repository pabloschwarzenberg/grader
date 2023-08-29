def buscarTodas(a, b):
    Lista_str = list(str(a).strip())
    Ubicaciones=[]
    for largo in range(len(Lista_str)):
        if Lista_str[largo]==str(b):
            Ubicaciones.append(str(largo))
    return (" ".join(Ubicaciones)).strip()
