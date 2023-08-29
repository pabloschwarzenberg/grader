def amigos(a,b):
    divisoresA=[]
    divisoresB=[]
    d=1
    g=1
    SDA=0
    SDB=0
    Friends=False
    while d<a:
        if a%d==0:
            divisoresA.append(d)
        d=d+1
    while g<b:
        if b%g==0:
            divisoresB.append(g)
        g=g+1
    for i in divisoresA:
        SDA+= i
    for i in divisoresB:
        SDB+= i
    if (SDA==b and SDB==a and a!=b):
        Friends=True
    return (Friends)