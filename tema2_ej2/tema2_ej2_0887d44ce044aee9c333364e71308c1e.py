# completa el código de la función
def suma(a,b):
       for i in range(1,a):
             if(a % i==0):
                    b=b+i
       return b
sum1,sum2=0,0
num1=int(input("ingrese primer numero:  "))
num2=int(input("ingrese segundo numero:  "))
sum1 = suma(num1, sum1)
sum2 = suma(num2, sum2)
if((sum1==num2)and (sum2==num1)):
       print("True")
else:
       print("False")
