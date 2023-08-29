def amigos(x,y):
    tot1=0
    tot2=0
    for i in range(1,x):
        if x%i==0:
            tot1+=i
 
    for k in range(1,y):
        if y%k==0:
            tot2+=k
    if tot1==y and tot2==x:
        resp=True
    else:
        resp=False
    return resp
 


