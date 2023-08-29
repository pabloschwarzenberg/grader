#Factores Primos

n=input("diga un número: ")
def num(n):
       for a in range (2,n):
         if n%a==0:
           for i in range(2,a-1):
               if a%i==0:
                   continue
                   
               else:
                    return a
                    