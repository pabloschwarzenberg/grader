# completa el código de la función
True
False
def amigos(a,b):
       for i in range(1,a):
             print("i",i,"rango", range(1,a))
             if(a % i==0):
                    print("valor a: ",a)
                    b=b+i
                    print("valor b: ",b)
       return b
amigos1,amigos2=0,0
n1=int(input("ingrese primer numero:  "))
n2=int(input("ingrese segundo numero:  "))
amigos1 = amigos(n1, amigos1)
amigos2 = amigos(n2, amigos2)
if((amigos1==n2)and (amigos2==n1)):
     print("los numeros "+str(n1)+" y "+str(n2)+" Si son numeros amigos")

else:
    print("los numeros "+str(n1)+" y "+str(n2)+" No son numeros amigos")



     