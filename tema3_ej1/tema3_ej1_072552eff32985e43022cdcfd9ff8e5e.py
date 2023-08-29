# completa el código de la función

if __name__ == "__main__":
    a=int(input("Ingrese un número: "))
    pass

divisores=[]
suma=0
def suma_divisores(a):
      for i in range(1, a): 
        if ((a%i)==0):
            divisores.append(i)
suma_divisores(a)
print(divisores)
for j in divisores:
    suma=suma+j
     
def es_primo(suma):
  if suma==1:
    return True
  else:
    return False
