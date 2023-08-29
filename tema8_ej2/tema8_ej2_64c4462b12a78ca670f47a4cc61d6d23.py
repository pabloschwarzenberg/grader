def buscarTodas(a,b):
    ret = ''
    for i in range(len(a)):
        if b == a[i] and i < len(a):
            ret = ret + str(i) + ' '
        else:
            pass
    if ret[len(ret)-1] == ' ':
        ret = ret[:len(ret)-1]
    return ret

if __name__ == "__main__":
    pass
           