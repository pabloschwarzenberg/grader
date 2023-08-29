n1=int(input('ingrese el primer numero:'))
n2=int(input('ingrese el segundo numero:'))
n3=int(input('ingrese el tecer numero:'))
if n1>n2 and n1>n3:
  if n2>n3:
    print(n3,',',n2,',',n1)
  else:
    print(n2,',',n3,',',n1)
if n2>n3 and n2>n1:
  if n3>n1:
    print(n1,',',n3,',',n2)
  else:
    print(n3,',',n1,',',n2)
if n3>n2 and n3>n1:
  if n1>n2:
    print(n2,',',n1,',',n3)
  else:
    print(n1,',',n2,',',n3)