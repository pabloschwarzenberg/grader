# completa el código de la función
def amigos(a,b):
  return
           
n=("ingrese un numero: ")
a=cont = 0
for a in range(1, 1000 + 1):
    for b in range(1, a + 1):
        if a % b == 0:
            cont = cont + 1
    if cont == 2:
        print("{}".format(a))
    cont=0

if(n==a):
  print("True")
else:
    print("false")