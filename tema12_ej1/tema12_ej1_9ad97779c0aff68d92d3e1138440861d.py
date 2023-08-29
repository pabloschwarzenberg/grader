lista=[0,1]
def generar(n,num):
  global lista
  if len(num)==n:
    print(num)
    return
  else:
    for i in lista:
      num.append(i)
      generar(n,num)
      num.pop()
n=int(input())
num=[]
generar(n,num)
  
  