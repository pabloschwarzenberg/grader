def numero_perfecto(p):
    suma = 0
    for i in range(1,p):
       if (p % (i) == 0):
          suma += (i)
    if p == suma:
       return True
    else:
       return False
if __name__=="__main__":
    p=int(input("Ingrese p: "))
    print(numero_perfecto(p))
           