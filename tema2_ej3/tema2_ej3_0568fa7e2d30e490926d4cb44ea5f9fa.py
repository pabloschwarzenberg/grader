def numero_perfecto(x):
    suma = 0
    for i in range(1,x):
       if (x % (i) == 0):
          suma += (i)
    if x == suma:
       return True
    else:
       return False

if __name__ =="__main__":
    x=int(input("Ingrese x: "))
    print(numero_perfecto(x))