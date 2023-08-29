a = 220
b = 284
def amigos(a,b):
    s=0
    t=0
    for n in range (1,a):       
        if a%n==0:
            s=s+n
    for n in range(1,b):
        if b%n==0:
            t=t+n   
    if s==b and t==a :
        return True
    else:
        return False
                
print(amigos(a,b))
