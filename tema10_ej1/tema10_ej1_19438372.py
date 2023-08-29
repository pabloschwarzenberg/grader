l1=[]
l2=[]
l3=[]
def mcm(a,b,c):  
    MCM=0
    n=2
    while n<=a:
        if a%n==0:
            l1.append(n)
            return mcm(a/n,b,c)
        else:
            n+=1

    while n<=b:
        if b%n==0:
            l2.append(n)
            return mcm(a,b/n,c)
        else:
            n+=1
                
                
    for j in l2:
        if j in l1:
            l3.append(j)
            l1.remove(j)

            
    resultado=1
    if len(l3)==0:
        MCM=c/resultado
        return MCM

    m=0
    while m<len(l3):
        resultado*=l3[m]
        m+=1

    MCM=c/resultado
    return MCM
