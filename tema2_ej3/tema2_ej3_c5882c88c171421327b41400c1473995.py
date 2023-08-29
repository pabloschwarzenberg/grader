def numero_perfecto(a):
    numero = a
    i = 1
    sumaDivisores = 0
    while (i < numero):
      if(numero % i == 0):
        sumaDivisores += i
      i += 1
    if(sumaDivisores == numero):
      return True
    return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           