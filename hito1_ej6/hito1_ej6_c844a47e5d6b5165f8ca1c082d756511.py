n1=input("ingresa un número: ")
n2=input("ingresa otro número: ")
n3=input("ingresa un tercer numero: ")

if n2<n3 and n1<n2:
      print(n1+","+n2+","+n3)
if n3<n2 and n1<n3:
      print(n1+","+n3+","+n2)
if n3<n1 and n2<n3:
      print(n2+","+n3+","+n1)
if n1<n2 and n3<n1:
      print(n3+","+n1+","+n2)
if n2<n1 and n1<n3:
      print(n2+","+n1+","+n3)
if n3<n2 and n2<n1:
      print(n3+","+n2+","+n1)
if n2==n3 and n1<n2:
      print(n1+","+n2+","+n3)
if n1==n2 and n1<n3:
      print(n1+","+n2+","+n3)
if n3==n1 and n3<n2:
      print(n1+","+n3+","+n2)
if n2==n3 and n1>n2:
      print(n3+","+n2+","+n1)
if n1==n2 and n1>n3:
      print(n3+","+n2+","+n1)
if n3==n1 and n3>n2:
      print(n2+","+n3+","+n1)

