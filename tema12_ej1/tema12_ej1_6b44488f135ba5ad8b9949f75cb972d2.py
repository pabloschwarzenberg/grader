#tu programa recibirá como parámetro un número que indicará el largo de las combinaciones de números binarios
#que se deben generar
n=int(input())
#cada combinación que tu programa genere usando backtracking debe imprimirla en una línea separada
#un ejemplo de combinación de largo 4 sería
a=""
for i in range(n):
  a=a+"1"
combs=[a]
def comb(n,a):
  if "1" not in a:
    global combs
    return
  else:
    for i in range(n):
      x=list(a)
      if a[i]=="1":
         x[i]="0"
      z="".join(x)
      if z not in combs:
          combs.append(z)
          comb(n,z)
comb(n,a)
for i in combs:
  print(i)
  


           