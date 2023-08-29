def amigos(a,b):
num1 = int(input("Primer numero: "))
num2 = int(input("Segundo numero: "))
       for i in range(2,a):
             if(a % i==0):
                    b=b+i
               sum1 = 1
               sum2 = 1
               sum1 = amigos(n1, sum1)
               sum2 = amigos(n2, sum2)
               if((sum1==n2)and (sum2==n1)):
                 return True
               else:
                return False
       return b