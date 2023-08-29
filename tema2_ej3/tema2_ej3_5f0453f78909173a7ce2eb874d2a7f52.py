def numero_perfecto(a):
    a=int(a)
    multiplos=[]
    for i in range(1,a):
        if a % i == 0:
            multiplos.append(int(i))
    if sum(multiplos)==a:
      return True
    else:  
      return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           