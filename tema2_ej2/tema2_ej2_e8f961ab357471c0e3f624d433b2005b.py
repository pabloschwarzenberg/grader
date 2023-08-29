def amigos(l1, l2):
    lamigos = []
    for i in sorted(l1):
        list_temp = []
        for j in sorted(l2):
            maxn = max(i, j) 
            minn = min(i, j) 
            un = int(str(maxn)[0] + (len(str(maxn)) - 1) * '0')
            if (minn in list(range(un, maxn)) and maxn > 99):
                list_temp.append(j)
        if (len(list_temp) > 0):
            lamigos.append([i] + list_temp)
    return lamigos