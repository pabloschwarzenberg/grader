def divisores(n,suma):
       for i in range(2,n):
             if(n % i==0):
                    suma+=i
       return suma
def amigos(a,b):
    sumA=1
    sumB=1
    sumA = divisores(a, sumA)
    sumB = divisores(b, sumB)
    if((sumA==b) and (sumB==a)):
           amigos=True
    else:
           amigos=False
    return amigos

           