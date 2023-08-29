# completa el código de la función
def amigos(a,b):
  if suma_divisores(a)==b and suma_divisores(b)==a:
    return True
  else:
    return False
def suma_divisores(n):
    divisor=1
    b=0
    while divisor<n:
        if n%divisor==0:
            b=b+divisor
        divisor =divisor+1
    return b