def buscarTodas(a,b):
    pal=[m for m,z in enumerate(a) if z==b]
    lista=list(pal)
    lista_1=[]
    for m in lista:
        lista_1.append(str(m))
    espacio=" ".join(lista_1)
    return espacio

if __name__ == "__main__":
    print(buscarTodas('tres tristes tigres','t'))
    pass