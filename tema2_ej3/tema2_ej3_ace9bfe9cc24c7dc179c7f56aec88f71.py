def numero_perfecto(num):
    i=1
    suma=0
    while i!=num:
        if num%i==0:
            suma=suma+i
        i+=1
    if suma==num:
        return True
    else:
        return False

if __name__ == "__main__":
  num=eval(input("Ingrese su numero: "))
  if numero_perfecto(num):
    print("El numero" +str(num)+" es Perfecto")
  else:
    print("El numero" +str(num)+"NO es Perfecto")
           