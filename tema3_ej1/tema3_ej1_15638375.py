# completa el código de la función
def suma_divisores(n):
    div=[1]
    i=2
    x=n
    while i<x:
        if n%i==0:
            div.append(i)
            n=n/i
            i-=1
        i+=1
    print (sum(div))
    if sum(div)==1 and x!=1:
        return (sum(div), True)
    elif x==1:
        div=[0]
        return (sum(div), False)
    else:
        return (sum(div), False)

           