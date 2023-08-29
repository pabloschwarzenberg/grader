import math

def es_primo(numb):
    if numb==2:
        return True
    if numb > 1:

        for i in range(2, numb):
            if (numb % i) == 0:
                return False
            else:
                return True
    else:
        return False

def mcm(a,b,ab):
    if a*b==1:
        return 1
    else:
        n=1
        while True:
           if es_primo(n)==True:
               count=0
               if a%n==0:
                   a=a//n
                   count=1
               if b % n == 0:
                   b = b // n
                   count=1
               if count==0:
                    n=n+1
               else:
                   break
           else:
               n=n+1
        return n * mcm(a, b, a * b)


if __name__ == "__main__":
    print(mcm(88,44,88*44))
    pass
