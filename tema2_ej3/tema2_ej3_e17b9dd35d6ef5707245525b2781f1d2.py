def numero_perfecto(a):
    divisores = []
    for i in range(1,a+1):
        if a % i == 0:
          divisores.append(i)
    suma = sum(divisores)
    resultado = suma - a
    if resultado == a:
        return True
    if resultado != a:
        return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           
