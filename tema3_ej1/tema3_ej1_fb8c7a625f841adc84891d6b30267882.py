def suma_divisores(a):
    divisores = []
    for i in range(1, a):
      if a % i == 0:
           divisores.append(i)

    
    return sum(divisores), len(divisores)== 1
print(suma_divisores(29))