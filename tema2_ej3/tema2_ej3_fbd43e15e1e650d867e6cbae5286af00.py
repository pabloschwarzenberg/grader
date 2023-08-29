def numero_perfecto(a):
    divisores = []
    for x in range(1, a):
      if a%x == 0:
        divisores.append(x)
    y = sum(divisores)
    if y == a:
      return True
    else:
      return False
if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))

           