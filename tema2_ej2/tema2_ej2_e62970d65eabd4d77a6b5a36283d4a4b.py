def amigos(a,b):
    i=1
    j=1
    sumaDivisores_a = 0
    sumaDivisores_b = 0
    while i<a:
        r = a%i
        if(r==0):
            sumaDivisores_a +=i
        i +=1

    while j<b:
        r = b%j
        if(r==0):
            sumaDivisores_b +=j
        j +=1
    return (sumaDivisores_a == b and sumaDivisores_b==a)