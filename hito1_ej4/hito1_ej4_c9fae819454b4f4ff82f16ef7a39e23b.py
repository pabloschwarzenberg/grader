num=int(input("ingrese un numero:"))
lista=[]
while num>=1:
  lista.insert(0,num%2)
  num=num//2
print("resultado=",end="")  
for i in lista:
  print(i,end="")
 