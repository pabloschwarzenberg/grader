# completa el código de la función
def amigos(a,b):
       for i in range(2,a):
             if(b % i==0):
                    b=b+i
       return b
sum1 = 1
sum2 = 1
n1=int(input("ingrese primer numero\n"))
n2=int(input("ingrese segundo numero\n"))
sum1=amigos(n1, sum1)
sum2=amigos(n2, sum2)

if((sum1==n2)and (sum2==n1)):
          print("los numeros "+str(n1)+" y "+
          str(n2)+" Si son numeros amigos")
else:
      print("los numeros "+str(n1)+" y "+
      str(n2)+" No son numeros amigos")


      
