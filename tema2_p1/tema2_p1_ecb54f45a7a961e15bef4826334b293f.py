def es_primo(numero):
    divisor=1
    i=0
    while divisor<=numero:
       if numero%divisor==0:
          i=i+1
       divisor = divisor + 1
    if numero==1 or numero==2:
       return False
    elif i==2:
       return True
    else:
       return False
           