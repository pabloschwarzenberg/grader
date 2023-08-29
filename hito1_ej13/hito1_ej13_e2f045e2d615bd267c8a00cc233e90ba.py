#Factores Primos

def Lol(n):
    a= 2
    while a*a<=n:
        if n%a:
            a+=1
        else:
            n//=a
            print(a)
    if n>1:
        print(n)

n= int(input())
Lol(n)      