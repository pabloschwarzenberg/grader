#Ordenar tres números
n1 = int(input("Ingrese un numero entero: "))
n2 = int(input("Ingrese otro numero entero: "))
n3 = int(input("Ingrese otro numero entero: "))
if n1 >= n2 and n1 >= n3 and n2 >= n3:
  print(n3,",",n2,",",n1)
else:
  if n1 >= n2 and n1 >= n3 and n3 >= n2:
    print(n2,",",n3,",",n1)
  else:
    if n2 >= n1 and n2 >= n3 and n1 >= n3:
      print(n3,",",n1,",",n2)
    else:
      if n2 >= n1 and n2 >= n3 and n3 >= n1:
        print(n1,",",n3,",",n2)
      else:
        if n3 >= n1 and n3 >= n2 and n1 >= n2:
          print(n2,",",n1,",",n3)
        else:
          if n3 >= n1 and n3 >= n2 and n2 >= n1:
            print(n1,",",n2,",",n3)


