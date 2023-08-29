#Ordenar tres números
n1 = eval(input("ingrese el primer numero"))
n2 = eval(input("ingrese el segundo numero"))
n3 = eval(input("ingrese el tercer numero"))

if(n1 < n2 < n3):
  print(n1, "," ,n2, "," ,n3)
else:
    if(n1 > n2 > n3):
      print(n1, "," ,n2, "," ,n3)
    else:
        if(n1 > n2 < n3):
          print(n1, "," ,n2, "," ,n3)
        else:
          if(n1 < n2 > n3):
            print(n1, "," ,n3, "," ,n2)