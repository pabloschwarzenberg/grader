n= int(input())
def numero_primo(n):
    if n==1:
         return False
    for i in range(2,n):
         if (n%i==0) and n!=2 :
             return False
    return True
                        
def factor_primo(n):
    if n==1:
        return False
    elif n==2:
        print(n)
    for a in range (2, n):
        if (n%a)==0 and numero_primo(a):
            print(a)
factor_primo(n)