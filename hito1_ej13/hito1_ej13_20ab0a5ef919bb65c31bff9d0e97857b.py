#Factores Primos
def es_primo(num):
    c=1
    f=0
    while(c<=num):
       if num%c == 0:
           f=f+1
       c=c+1
    if(f==2):
        return True
    else:
        return False
    
n=int(input("numero "))
c=1
while (c<=n):
    if(es_primo(c)):
        if(n%c==0):
            print(c)
    c=c+1      