numero=int(input())
largo=len(str(numero))
binario= ""
while largo>0:
  a=numero%2
  aa=str(a)
  b=numero//2
  binario+=aa
  numero=b
  if b<10**(largo-1):
    largo-=1
print("resultado="+binario[::-1])