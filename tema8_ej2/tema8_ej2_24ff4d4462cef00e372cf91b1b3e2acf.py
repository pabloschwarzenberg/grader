def buscarTodas(a, b):
    lis = []
    for i in range(len(a)):
        if (b == a[i]):
            lis.append(i)
    x= lis[-1]
    y= str(lis)
    w= y.replace(",", "")
    w= w.replace("[","")
    w= w.replace("]","")
    return w
if __name__ == "__main__":
    a = "tres tristes tigres"
    b = "t"
    print(buscarTodas(a, b))