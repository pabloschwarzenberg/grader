def subsecuencia(string,numero_entero):
  lista=[]
  for i in range(len(string)):
    if i!=len(string)-2:
      lista.append(string[i:i+numero_entero])
  for elemento in lista:
    if lista.count(elemento)==1:
      print(elemento)
    else:
      print("ninguna")
n=input()
e=int(input())
subsecuencia(n,e)
    
