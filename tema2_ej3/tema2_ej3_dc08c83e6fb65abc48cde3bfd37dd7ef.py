def numero_perfecto(a):
    divisor=2
    suma=1
    primo=False
    if a==1:
        return False
    while divisor<a:
        if a%divisor==0:
            suma=divisor+suma
        divisor=divisor+1
    if suma==a:
      return True
    else:
      return False

           