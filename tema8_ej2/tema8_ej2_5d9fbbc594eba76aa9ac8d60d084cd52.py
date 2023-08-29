def buscarTodas(a,b):
    a = a.lower()
    b = b.lower()
    str1 = ""
    for k in range(len(a)):
        if a[k] == b:
            str1 += str(k)+" "
    str2 = str1[:-1]
    return str2

if __name__ == "__main__":
    pass
           