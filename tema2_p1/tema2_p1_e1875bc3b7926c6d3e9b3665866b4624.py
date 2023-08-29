def es_primo(n):
    divisor=1
    cant_divisores=0
    while n>=divisor :
        if n%divisor==0:
            cant_divisores=cant_divisores+1
        divisor = divisor + 1
    if cant_divisores==2 :
         return True
    else:
         return False



           