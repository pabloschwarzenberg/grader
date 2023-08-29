ent=int(input())
for i in range(2, ent):
    b=0
    for j in range(1, (i//2)+1):
        if((i%j)==0):
            b= b+j;
    if(b==i):
        return True
    else:
        return False