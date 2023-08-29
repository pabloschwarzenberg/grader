# completa el código de la función
def amigos(a,b):

    divisor_a=1
    divisor_a=int(divisor_a)
    
    divisor_b=1
    divisor_b=int(divisor_b)
    
    suma_a=0
    suma_a=int(suma_a)
    suma_b=0
    suma_b=int(suma_b)

    pa=1
    pa=int(pa)
    pb=1
    pb=int(pb)

    while divisor_a<a:

        pa=a%divisor_a

        if pa==0:

            suma_a=suma_a+divisor_a

        divisor_a=divisor_a+1

    while divisor_b<b:

        pb=b%divisor_b

        if pb==0:

            suma_b=suma_b+divisor_b

        divisor_b=divisor_b+1

    if suma_a==b and suma_b==a:

        return True

    if suma_a!=b or suma_b!=a:

        return False
  
           