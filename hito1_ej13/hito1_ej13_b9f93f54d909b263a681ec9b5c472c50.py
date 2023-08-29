numero = int(input("Ingrese Su Número: "))

c=2

while c<=numero:

  if numero%c==0:

    print(c)

    numero = numero/c

  else:

    c+=1