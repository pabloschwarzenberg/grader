# por favor escribe aquí tu función
print("Hola estudiante")
def es_primo(num):

  if num >1:

    a=0

    divisor=2

    while divisor<num:

      resto = num%divisor

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

  num_ingreso = int(input("Ingrese número: "))

  print(es_primo(num_ingreso))

except:

  print("Ingrese sólo número por favor")
           