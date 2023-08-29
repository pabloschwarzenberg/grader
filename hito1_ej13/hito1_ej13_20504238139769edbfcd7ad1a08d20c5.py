#Factores Primos
b=int(2)
a=int(input("ingrese un numero"))
while(a!=1):
    if(a%b==0):
      print(str(b)+"")
      a=a/b
    else:
        b=b+1     