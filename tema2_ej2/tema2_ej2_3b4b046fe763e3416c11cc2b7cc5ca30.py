def amigos(a,b):
    i,j=1,1
    s_a,s_b=0,0
    while i<a :
        if a%i==0 :
            s_a=s_a+i
        i=i+1
    while j<b :
        if b%j==0 :
            s_b=s_b+j
        j=j+1
    if s_a==b and s_b==a :
        return True
    else:
         return False