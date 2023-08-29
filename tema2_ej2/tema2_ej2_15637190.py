def amigos(a,b):
    i=1
    j=1
    sumaA=0
    sumaB=0

    while i<a:
        if a%i==0:
          sumaA+=i
        i+=1
    print(sumaA)
    while j<b:
        if b%j==0:
          sumaB+=j
        j+=1
    print(sumaB)
    if sumaB==a and  b== sumaA:
        return True
    else:
        return False
           