numero = float(input("Introduce el número: "))
umil = numero / 1000
tmp = numero % 1000
centenas = tmp / 100
tmp = tmp % 100
decenas = tmp / 10
unidades = tmp % 10
print("M: %i" % umil)
print("C: %i" % centenas)
print("D: %i" % decenas)
print("U: %i" % unidades)
if umil<=0:
  print(centenas, "C + ",decenas, "D +", unidades, "U")
  if centenas<=0:
      print(decenas, "D +", unidades, "U")
  if decenas<0:
       print(unidades, "U")
if umil>0:
 print("%i" % umil, "M +", "%i" % centenas, "C +","%i" % decenas, "D +",
"%i" % unidades, "U")

#numeros primos

def es_primo(num):
    if num<2:
      return False
    for i in range(2, num):
      if num%i==0:
         return False
    return True
print(es_primo(3))