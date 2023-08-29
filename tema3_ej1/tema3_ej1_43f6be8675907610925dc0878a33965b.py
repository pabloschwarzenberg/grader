# completa el código de la función

def suma_divisores(n):
    divisor=1
    b=0
    while divisor<n:
        if n%divisor==0:
            b=b+divisor
        divisor =divisor+1
    
    return (b,es_primo(n))

def divisores(n):
    divisor=1
    cantidad_divisores=0
    while divisor<=n:
        if n%divisor==0:
            cantidad_divisores=cantidad_divisores+1
        divisor=divisor+1
    return cantidad_divisores

def es_primo(n):
    if divisores (n)==2:
        return True
    else:
        return False


if __name__ == "__main__":
  n=int(input())
  print(suma_divisores(n))
