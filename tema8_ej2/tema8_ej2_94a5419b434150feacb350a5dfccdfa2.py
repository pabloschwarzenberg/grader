def buscarTodas(a,b):
    w=[m for m,z in enumerate(a) if z==b]
    lis=list(w)
    lis_1=[]
    for m in lis:
        lis_1.append(str(m))
    espacio=" ".join(lis_1)
    return espacio

if __name__ == "__main__":
    print(buscarTodas('tres tristes tigres','t'))
    pass