#Alexander
a = int(input("Numero 1: "))
b = int(input("Numero 2: "))
c = int(input("Numero 3: "))

if a > b:
  aux = a ; a = b ; b = aux
if a > c :
  aux = a ;a = c ; c = aux
if b > c :
  aux = b ; b = c ; c = aux
print ("de menor a mayor", a, b, c)