def buscarTodas(a,b):
    i = 0
    res = ""
    for i in range(len(a)):
        if (a[i] == b):
            res = res + str(i) + " "

    for i in range(len(a)):
        if (a[i] == " "):
            pass

    return res.rstrip()

if __name__ == '__main__':
    res = buscarTodas('tres tristes tigres','t')
    print(res)