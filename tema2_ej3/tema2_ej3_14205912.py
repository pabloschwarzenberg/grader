def numero_perfecto(a):
    i=1
    suma_div_a=0
    while i<a:
        if a%i==0:
            suma_div_a+=i
        i+=1 
    return (suma_div_a==a)