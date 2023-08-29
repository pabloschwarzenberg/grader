def mcd(a,b):
    numeros=list((a,b))
    numeros.sort()
    if a==0 and b!=0:
      return b
    elif a!=0 and b==0:
      return a
    else:
      mayor=numeros[0]
      menor=numeros[1]
      factor=mayor//menor
      residuo=mayor%menor
      resultado=mcd(factor,residuo)
      return resultado
      
def mcm(a,b,ab):
    divisor=mcd(a,b)
    resultado=ab/divisor
    return resultado


if __name__=="__main__":
    pass
           