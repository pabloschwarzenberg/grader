n1=float(input("Ingrese su primer numero"))
n2=float(input("Ingrese su segundo numero"))
n3=float(input("Ingrese su tercer numero"))
  if n1<n2<n3:
    print(n1,n2,n3,)
  elif n1<n3<n2:
    print(n1,n3,n2,)
  elif n2<n1<n3:
    print(n2,n1,n3,)
  elif n2<n3<n1:
    print(n2,n3,n1,)
  elif n3<n1<n2:
    print(n3,n1,n2,)
  elif n3<n2<n1:
    print(n3,n2,n1,)
  else:
    print("Numeros no Validos")     