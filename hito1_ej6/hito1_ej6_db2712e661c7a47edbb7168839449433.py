#Ordenar tres números
n1=input("Ingrese Numero X: ")
n2=input("Ingrese Numero Y: ")
n3=input("Ingrese Numero Z: ")
#3-1-2/2-1-3/2-3-1


if n1 <= n2 <= n3:
  print(n1,",",n2,",",n3)
else:
  if n3<=n2<=n1:
    print(n3,",",n2,",",n1)
  else:
    if n1<=n3<=n2:
      print(n1,",",n3,",",n2)
    else:
      if n3<=n1<=n2:
        print(n3,",",n1,",",n2)
      else:
        if n2<=n1<=n3:
          print(n2,",",n1,",",n3)
        else:
          if n2<=n3<=n1:
            print(n2,",",n3,",",n1)



