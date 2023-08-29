#Ordenar tres números
print('Ingrese el primer número:')
n1 = int(input())
print('Ingrese el segundo número:')
n2 = int(input())
print('Ingrese el tercer número:')
n3 = int(input())
print()
print('Los números ingresados de menor a mayor son:')
if n1 <= n2 <= n3:
  print(n1,',',n2,',',n3) 
elif n1 <= n3 <= n2:
  print(n1,',',n3,',',n2)

elif n2 <= n1 <= n3:
      print(n2,',',n1,',',n3)
 
elif n2 <= n3 <= n1:
        print(n2,',',n3,',',n1)

elif n3 <= n1 <= n2:
          print(n3,',',n1,',',n2)

else:
           print(n3,',',n2,',',n1)

