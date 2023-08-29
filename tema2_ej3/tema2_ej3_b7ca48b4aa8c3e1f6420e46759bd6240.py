def numero_perfecto(a):
    divisores = []
    for i in range(1, a):
      if a % i == 0:
        i = divisores.append(i)
    
    suma = 0
    for divisor in divisores:
      suma = suma + divisor
    if suma == a: 
      EsPerfecto = True
    else:
      EsPerfecto = False
    return EsPerfecto

if __name__=="__main__":
  n=int(input("Ingrese a: "))
  print(numero_perfecto(n))          