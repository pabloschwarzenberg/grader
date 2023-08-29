def numero_perfecto(a):
  divisor = [1]
  for i in range(2, a):
    if a % i == 0:
      divisor.append(i)
  if sum(divisor) == a:
    return True
  else:
    return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           