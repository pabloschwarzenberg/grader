# completa el código de la función

primo=True
def suma_divisores(a):
    numero=[]
    i=2
    while i<=a:
          if a%i==0:
              x=a//i
              numero.append(x)
          i=i+1
    numesum=(sum(numero))
    if numesum==1:
        primo=True
        return (numesum, primo)
    if numesum!=1:
        primo=False
        return (numesum, primo)
           