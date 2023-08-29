def rot13(palabra):
    camb = "nopqrstuvwxyzabcdefghijklm"
    new = ""
    k = 0
    n = 0
    while k != len(palabra):
        while n != len(camb):
            if(palabra[k] == camb[n]):
                new += camb[n]
                n += 1
            else:
                n += 1
        k += 1
    return(new)