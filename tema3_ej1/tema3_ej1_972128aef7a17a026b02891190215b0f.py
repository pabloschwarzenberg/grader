# completa el código de la función
def suma_divisores(a):
    z = []
    for x in range(1, a):
        if a % x == 0:
           if a == x:
               z.append(0)
           else:
               z.append(x)
    w = False
    print(sum(z)%a)
    if sum(z) >= 1:
        if sum(z) == 1:
            w = True
        elif sum(z) == 0:
            w = True
            
    return(sum(z), w)
    
    
           