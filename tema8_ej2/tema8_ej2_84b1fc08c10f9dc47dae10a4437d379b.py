def buscarTodas(a,b):
    lis = []

    for pos, carac in enumerate(a):
        if carac == b:
            lis.append(pos)
    
    string = " ".join(map(str, lis))
    
    return string

if __name__ == "__main__":
    pass
           