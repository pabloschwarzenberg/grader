#Ordenar tres números
      V=int(input("ingrese el primer numero:"))
      I=int(input("ingrese el segundo numero:"))
      C=int(input("ingrese el tercer numero:"))
      
      A=min(V,I,C)
      C=max(V,I,C)
      B=(V + Y + Z)-A-C
      
      print("los numeros de menor a mayor son: {},{}y{}".format(A,B,C))
      