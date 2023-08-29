def nprimo(numero):
    
  if numero >1:

    a=0

    divisor=2

    while divisor<numero:

      resto = numero%divisor

      if resto==0:

        a+=1

      divisor+=1

    if a==0:

      return True

    else:

      return False

  else:

    return False



try:

  numingreso = int(input("Favor ingrese un numero: "))

  print(nprimo(numingreso))

except:

print("Por favor solo ingresar numeros")