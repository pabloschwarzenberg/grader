def suma_divisores(a):
    cantidad = 0
    for x in range(1, a):
       if a % x == 0:
            cantidad += x
    return cantidad
 
def numero_perfecto(a):
    if suma_divisores(a )== a:
      return True
    else:
      return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
    pass      