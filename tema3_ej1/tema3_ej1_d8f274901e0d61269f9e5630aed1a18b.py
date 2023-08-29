# completa el código de la función
def suma_divisores(a):
    dividir = [1]
    #for
    for i in range(2, a + 1):
        if a %i == 0:
            #appened
            dividir.append(i)
    #numeros primos
    if a >1:
        x=0
        divisor=2
        while divisor<a:
          resto = a%divisor
          if resto==0:
            x+=1
          divisor+=1
          #True
        if x==0:
          primo = True
          #False
        else:
          primo = False
     #False
    else:
        primo = False
    
    return (sum(dividir)-a,primo)

           