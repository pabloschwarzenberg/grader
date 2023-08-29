def numero_perfecto(a):
    divisores=[]
    divisor=1
    suma=0
    while a > divisor:
          if a%divisor == 0:
             divisores.append(divisor)
          divisor += 1
    for i in divisores:
        suma += i
        if suma == a:
           return True
    return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           