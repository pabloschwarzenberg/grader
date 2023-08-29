def es_primo(num):
    count=0
    i=1
    while i<=num:
        c=num/i
        if c==1 or c==num:
            count+=1
        i+=1
    if count==2:
        return True
    else:
        return False