def suma_divisores(x):
    suma=0
    valor=1
    for i in range(1,(x//2)+1):
      if x%i==0:
        suma+=i
    return suma

def amigos(x,y):
    if x == suma_divisores(y) and y == suma_divisores(x):
        return True
    else:
        return False

if __name__=="__main__":
    a=int(input("Ingrese un numero: "))
    b=int(input("Ingrese otro numero:"))
    numeros_amigos(a,b)