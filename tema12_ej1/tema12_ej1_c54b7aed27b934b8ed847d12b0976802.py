def numeros_binarios(num,s,lis):
    if len(s)>=num:
        if len(s)==num:
            lis.append(s)
        return lis.copy()
    l=["0","1"]
    for n in l:
        s=s+n
        lis=numeros_binarios(num, s, lis)
        s=s[0:len(s)-1]
    return lis

n = int(input())
a=numeros_binarios(n,"",[])
for c in a:
    print(c)