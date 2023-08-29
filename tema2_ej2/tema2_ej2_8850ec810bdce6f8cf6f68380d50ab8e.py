a=input("ingrese el primer numero amigo")
b=input("ingrese el segundo numero amigo")

def suma(a,b):
       for i in range(2,b):
             if(b % i==0):
                    a=a+i
       return a
sum1,sum2=1,1

sum1 = suma(amigo1, sum1)
sum2 = suma(amigo2, sum2)
if((sum1==amigo2)and (sum2==amigo1)):
       print(True)
else:
       print(False)