# completa el código de la función

def amigos(a, b):
    lamigos = []
    for i in sorted(a):
        list_temp = [] 
        for j in sorted(b):
            maxn = max(i, j) 
            minn = min(i, j)
            un = int(str(maxn)[0] + (len(str(maxn)) - 1) * '0')
            if (minn in list(range(un, maxn)) and maxn > 99):
                list_temp.append(j)
        if (len(list_temp) > 0):
            lamigos.append([i] + list_temp)
    return lamigos
print(amigos)