def amigos(a,b):
    sx=0
    sy=0
    for i in range(1,a):
        if a%i==0:
            sx+=i
 
    for k in range(1,b):
        if b%k==0:
            sy+=k
 
    return sx==b and sy==a
     
 

  