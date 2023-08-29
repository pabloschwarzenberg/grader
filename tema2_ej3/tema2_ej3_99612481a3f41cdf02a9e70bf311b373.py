ent = int(input())
for i in range(2, ent+1):
    b=0
    for j in range(1, (i//2)+1):
        if((i%j)==0):
            b= b+j;
    if(b==i):
        print("%s es perfecto" %i)
    else:
        print("%s no es perfecto" %i)