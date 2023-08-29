def numero_perfecto(a):
    sum_a=0
    for i in range(1,a):
      if a%i==0:
        sum_a=sum_a+i
    if a==sum_a:
      return True
    else:
      return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           