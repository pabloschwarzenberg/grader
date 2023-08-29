if __name__ == "__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
    pass
    
divisores=[]
suma=0
def suma_divisores(a):
      for i in range(1, a): 
        if ((a%i)==0):
            divisores.append(i)
suma_divisores(a)

for j in divisores:
    suma=suma+j
def numero_perfecto(suma,a):
    if suma==a:
        return True
    else:
        return False
   

