def numero_perfecto(a):
    k = 0
    if a == 1:
      return True
    for i in range(1,a):
      if a % i == 0:
        k += i
    if k == a:
      return True
    else:   
      return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           