# completa el código de la función
def amigos(a,b):
    div1=1
    sum1=0
    while div1!=a:
        if a%div1==0:
            sum1+=div1
        div1+=1
    div2=1
    sum2=0
    while div2!=b:
        if b%div2==0:
            sum2+=div2
        div2+=1
    return (sum1==b and sum2==a)
if __name__ == "__main__":
  a=int(input("ingrese el primer numero"))
  b=int(input("ingrese el segundo numero"))
  print(amigos(a,b))
           