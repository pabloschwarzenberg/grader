def agregar(n,l):
        l=l.copy()
        if len(l[-1])==n:
            return l
        else:
            a=[]
            for i in range(len(l)):
                a.append(l[i]+'1')
                a.append(l[i]+'0')
            a=a.copy()
            return agregar(n,a)

n=int(input())
for x in agregar(n,['0','1']):
    print(x)
