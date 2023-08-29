def buscarTodas(a,b):
    nuevo = ""
    for i in range(len(a)):
        if a[i] == b:
            if i == 0:
                nuevo += str(i)
            else:
                nuevo += " " + str(i)
    return nuevo

if __name__ == "__main__":
    pass
           