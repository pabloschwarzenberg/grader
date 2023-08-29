#Factores Primos
a=int(input(""))
for i in range(a):
  if a%(i+1)==0:
    aa=i+1
    div1=0
    for j in range(aa):
      if aa%(j+1)==0:
        div1=div1+(j+1)
        if div1==aa+1:
          print(aa)
            