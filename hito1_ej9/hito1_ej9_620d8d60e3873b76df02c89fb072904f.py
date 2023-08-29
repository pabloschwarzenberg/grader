a1 = float(input('Ingresa el primer valor: '))
b1 = float(input('Ingresa el segundo valor: '))
c1 = float(input('Ingresa el tercer valor: '))
a2 = float(input('Ingresa el cuarto valor: '))
b2 = float(input('Ingresa el quinto valor: '))
c2 = float(input('Ingrsa el sexto valor: '))

if a1/a2==b1/b2 and b1/b2==c1/c2:

  print("Infinitas soluciones")

elif a1/a2==b1/b2 and b1/b2!=c1/c2:

  print("No tiene solución")

else:

  x=(c1*b2-c2*b1)/(a1*b2-a2*b1)

  y=(a1*c2-a2*c1)/(a1*b2-a2*b1)

  print("x=", round(x,1))

  print("y=", round(y,1))
  
      