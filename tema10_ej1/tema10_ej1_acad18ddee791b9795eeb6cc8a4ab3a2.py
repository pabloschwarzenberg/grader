def mcm(a,b,c):
    l_a=[]
    l_b=[]
    for i in range(1,1000):
        c=a*i
        l_a.append(c)
    for i in range(1,1000):
        c=b*i
        l_b.append(c)
    for i in l_a:
        for n in l_b:
            if n==i:
                return n
            
            

if __name__=="__main__":
    pass