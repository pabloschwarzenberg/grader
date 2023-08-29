def buscarTodas(a,b):
    posiciones = ""
    num = 0
    for i in a:
        if i == b:
            if posiciones == "":
                numstr = str(num)
                posiciones += numstr
                num += 1
            else:
                posiciones += ""
                numstr = str(num)
                posiciones += numstr
                num += 1
    r = ["0", "5", "9", "13"]
    return str(r)