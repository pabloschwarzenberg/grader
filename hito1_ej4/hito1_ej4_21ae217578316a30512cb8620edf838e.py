#Conversión de Decimal a Binario
ent = int(input())
num = ent
res=''
while num != 0:
  res =res +str(num %2)
  num = num//2
res = res[::-1]
res = 'resultado='+ res
print(res)