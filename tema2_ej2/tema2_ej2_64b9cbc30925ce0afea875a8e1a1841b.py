def amigos(a,b):
    divisores_a=[]
    al = 0
    bl = 0
    if a==b:
        return False
    for i in range(1,a+1):
        if a % i == 0:
            divisores_a.append(i)
    divisores_b = []
    for i in range(1, b + 1):
        if b % i == 0:
            divisores_b.append(i)
    for i in divisores_a:
        for v in divisores_a:
            if i==v:
                pass
            else:
                if divisores_a[v]+divisores_a[i]==b:
                    al=al+1

    for i in divisores_b:
        for c in divisores_b:
            if c==i:
                pass
            else:
                if divisores_b[c]+divisores_b[i]==a:
                    bl=bl+1
    if al>=1 and bl>=1:
        return True
    else:
        return False   
