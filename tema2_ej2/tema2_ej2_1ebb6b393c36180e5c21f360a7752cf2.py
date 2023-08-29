def amigos(a,b):
    i=0
    j=0
  for i in range(1,a):
    if a%i==0:
      i+=i
  for j in range(1,b+1):
    if b%i==0:
      j+=j
  if j==i:
    print("True")
  else:
    print("False")
A= int(input("ingrese primer numero"))
B= int(input("ingrese el segundo numero"))

numeros_amigos= amigos(A,B)
print(numeros_amigos)
