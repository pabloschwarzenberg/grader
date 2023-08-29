#Contestador de celular
num=int(input())
hll=int(input())
if 0<=hll<=7:
  print(CONTESTAR)
a=num%1000
if 7<hll<14:
  if a==909:
    print('CONTESTAR')
  else:
    print('NO CONTESTAR')
num877= num/100000
l=round(num877,0)
f=int(l)
if 14<hll<17:
  print('NO CONTESTAR')
if 17<hll<19:
  print('NO CONTESTAR')
if 17<hll<19 and f==877:
  print('NO CONTESTAR')
if hll>19:
  print('NO CONTESTAR')