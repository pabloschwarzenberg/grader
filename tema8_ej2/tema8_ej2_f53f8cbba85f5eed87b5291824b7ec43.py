def buscarTodas(a,b):
    x=[]
    for i,c in enumerate(a):
        if c == b:
            x.append(str(i))
    cadena=" ".join(x)
    return cadena


if __name__ == "__main__":
    print(buscarTodas('tres tristes tigres','t'))       