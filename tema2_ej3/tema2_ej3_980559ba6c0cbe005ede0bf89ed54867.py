def numero_perfecto(a):
    l = []
    for i in range(1,a + 1):
      x = a % i
      if x == 0:
        l.append(i)
    l.remove(a)
    x = sum(l)
    if x == a:
      return True
    else:
      return False

'''if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))'''
           