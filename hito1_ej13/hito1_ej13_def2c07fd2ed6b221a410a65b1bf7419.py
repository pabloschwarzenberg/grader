#Factores Primos
n=int(input("numero: "))
def primo(n):
       l = []
       j = 2
       x=0
       while j*j <= n:
           while (n % j) == 0:
               l.append(j)  
               n//=j
           j += 1
       if n > 1:
          l.append(n)
       while x<=len(l)-1:
            a=l[x]
            x=x+1
            print(a)            
primo(n)
      