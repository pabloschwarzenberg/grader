def buscarTodas(a, b):
    indices = ""
    for i in range(0,len(a)):
        if(a[i] == b):
            indices += str(i)+" "
    return indices.strip()

if __name__ == "__main__":
    print(buscarTodas("tres tristes tigres","t"))
           