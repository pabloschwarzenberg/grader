n=int(input())
def combinaciones(cumplen,a_ver,n):
    if len(a_ver)==n:
        es=a_ver.copy()
        pala="".join(es)
        if pala not in cumplen:
            cumplen.append(pala)
        else:
            return

    else:
        for elem in ["0","1"]:
            a_ver.append(elem)
            combinaciones(cumplen,a_ver,n)
            a_ver.pop()
    return cumplen

hey=combinaciones([],[],n)
for elem in hey:
    print(elem)
