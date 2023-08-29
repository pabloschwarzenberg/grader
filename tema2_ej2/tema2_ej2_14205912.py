def amigos(a,b):
    i=1
    suma_div_a=0
    while i<a:
        if a%i==0:
            suma_div_a+=i
        i+=1
    j=1
    suma_div_b=0
    while j<=b:
         if b%j==0:
            suma_div_b+=j
         j+=1
    return (suma_div_b==a or suma_div_a==b)