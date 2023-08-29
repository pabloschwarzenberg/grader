
def numero_perfecto(a):
    numero=[]
    i=2
    while i<=a:
          if a%i==0:
              x=a//i
              numero.append(x)
          i=i+1
    numesum=(sum(numero))
    if numesum==a:
        return True
    if numesum!=a:
        return False