def es_primo(numero):
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
  numero_ingreso = int(input("Ingrese número: "))
  print(es_primo(numero_ingreso))
except:
  print("Ingrese sólo número")
 numero = float(input("Ingresa el número de 4 cifras: "))

print (" ")

umil = numero / 1000
tmp = numero % 1000

centenas = tmp / 100
tmp = tmp % 100

decenas = tmp / 10
unidades = tmp % 10

print ("Descomposición Horizontal")
print (" ")

print ("[","%i"%umil,"M +","%i" % centenas,"C +","%i" % decenas,"D +","%i" % unidades,"U","]")