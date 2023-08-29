def numero_perfecto(a):
    b = int(a)
    suma = 0
    
    for i in range(1, b):
      if b%i == 0 and i<b:
        suma = suma + i
    if suma == b:
      return True
    else:
      return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))

           