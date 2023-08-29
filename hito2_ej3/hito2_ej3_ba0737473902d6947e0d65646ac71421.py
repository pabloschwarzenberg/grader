string=input("")
n=int(input(""))
def subsecuencias_adn(string,n):
    x= string
    g=[]
    for i in range(0,len(string)):
        y=x[i:len(x)]
        for j in range(0,len(y)):
            g.append(y[:j+1])

    g2=[]
    for i in range(0,len(g)):
        count=0
        for j in range (0,len(g)):
            if g[i]==g[j]:
                count=count+1
        if count==1:
            g2.append(g[i])
    g3=[]
    for i in range(0,len(g2)):
        if len(g2[i])==n:
            g3.append(g2[i].lower())
    if len(g3)!=0:
        return g3
    else:
        return "ninguna"

print(subsecuencias_adn(string,n))