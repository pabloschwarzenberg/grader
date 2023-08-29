

import math


def dec_a_bin(a,n):
    if a==0:
        return "0"*n
    else:
        real=int((math.log(a,2))+1)
        l=[]
        chile=True
        while chile==True:

            l.append(str(a%2))
            a=a//2
            if a==0:
                chile=False
        for i in l:
            i=str(i)

        dif=n-real
        return "".join(l)+"0"*dif

n=input("ingrese un n: ")
def comb(n):
    n=int(n)
    max=(2**n)-1
    for i in range(max+1):
        print(dec_a_bin(i,n))
comb(n)




 

