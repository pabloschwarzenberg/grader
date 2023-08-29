def numero_perfecto(a):
    sum = 0
    for i in range(1,a):
      if a%i == 0:
          sum+=i
    if sum == a:
      return True
    else:
       return False

if __name__=="__main__":

    a=int(input("Ingrese valor de a: "))
    print(numero_perfecto(a))
