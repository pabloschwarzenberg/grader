x = int(input("Ingrese Número: "))

y=2

while y<=x:

  if x%y==0:

    print(y)

    x = x/y

  else:

    y+=1