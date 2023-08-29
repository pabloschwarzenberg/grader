# completa el código de la función
def suma_divisores(a):
    div = []
    for i in range(1, a):
      if a % i == 0:
           div.append(i)

    
    return sum(div), len(div)== 1