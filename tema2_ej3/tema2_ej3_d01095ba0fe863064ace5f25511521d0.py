def numero_perfecto(a):
    import math
    divisores=1
    lista_divisores=[]
    while a > divisores:
       if a%divisores==0:
          lista_divisores.append(divisores)
       divisores += 1
    suma=math.fsum(lista_divisores)
    if suma == a:
       return True
    else:
       return False
       
if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           