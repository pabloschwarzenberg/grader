def buscarTodas(a,b):
    x, y = 0, 2
    n = ""
    string = ""
    while 0 < 1:
        x = a.find(b, x)
        if x != -1:
            n = string
            string = string + str(x) + " "
        else:
            n = n + str(y)
            break
        y, x = x, (x + 1)
        
    return n

if __name__ == "__main__":
    pass
           