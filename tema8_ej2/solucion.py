def buscarTodas(a,b):
    r=""
    p=[]
    for i in range(len(a)):
        if a[i] == b:
            p.append(str(i))
    return " ".join(p)

if __name__ == "__main__":
    print(buscarTodas("tres tristes tigres","t"))
