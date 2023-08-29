def numero_perfecto(a):
    div1=1
    sum1=0
    while div1!=a:
        if a%div1==0:
            sum1+=div1
        div1+=1
   
    return (sum1==a)

if __name__=="__main__":
    a=int(input("ingrese el primer numero: "))
    b=0
    while b<=a:
      b+=1
      if numero_perfecto(b):
        print (b)
           