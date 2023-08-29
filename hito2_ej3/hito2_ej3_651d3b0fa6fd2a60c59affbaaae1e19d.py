def sub_secuencia(s,n):
  s=s.lower()
  i=0
  a=[]
  while i<len(s):
    if i+n>len(s):
      break
    a.append(s[i:i+n])
    i=i+1
  h=0
  #print(a)
  while h<len(a):
    z=a[h]
    if a.count(z)>1:
        b=a.count(z)
        k=0
        while k<b:
            a.remove(z)
            k=k+1
            h=h-1
            if h<0:
                h=0
    h=h+1
  if len(a)==0:
    a.append("ninguna")
  return a

#En este caso el programa debe recibir sus parámetros a través de input
secuencia=input("Ingrese la secuencia: ")
largo=int(input("Ingrese el largo: "))
l=sub_secuencia(secuencia,largo)
#se debe imprimir cada secuencia en una línea separada
for s in l:
    print(s)
