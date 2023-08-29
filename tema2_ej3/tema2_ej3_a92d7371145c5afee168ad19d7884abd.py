def numero_perfecto(a):
    j=0
    for i in range(1,a):
        if a%i ==0:
            j=j+i
    if j==a:
      return True
    if j != a:
      return False 

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           