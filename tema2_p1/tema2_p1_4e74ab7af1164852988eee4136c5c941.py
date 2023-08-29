def espar(n):
          if n%2 == 0:
                    return True
          else:
                    return False

numero = [1,2,3,4,5,6,7,8]
pares = list(filter(espar,numero))
print(pares)