#Factores Primos
def factorprimo(n):
    contador=0
    while contador==0:
        if n%2==0:
            n=n/2
            print(2)
        if n==1:
            break
        elif n%3==0:
            n=n/3
            print(3)
        elif n%5==0:
            n=n/5
            print(5)
        elif n%7==0:
            n=n/7
            print(7)
        elif n%11==0:
            n=n/11
            print(11)
        elif n%13==0:
            n=n/13
            print(13)
        elif n%17==0:
            n=n/17
            print(17)
        elif n%19==0:
            n=n/19
            print(19)
            # 23, 29, 31, 37,
        elif n%23==0:
            n=n/23
            print(23)
        elif n%29==0:
            n=n/29
            print(29)
        elif n%31==0:
            n=n/31
            print(31)
        elif n%37==0:
            n=n/37
            print(37)
        
        
        
            
a=int(input('ingrese valor:'))
factorprimo(a)
      