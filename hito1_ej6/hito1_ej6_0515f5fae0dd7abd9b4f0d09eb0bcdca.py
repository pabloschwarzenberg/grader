n1 = eval(input('numero 1: '))
n2 = eval(input('numero 2: '))
n3 = eval(input('numero 3: '))

if n1 <= n2 <= n3:
  print(n1,',',n2,',',n3)
elif n1 <= n3 <= n2:
  print(n1,',',n3,',',n2)
elif n2 <= n1 <= n3:
  print(n2,',',n1,',',n3)
elif n2 <= n3 <= n1:
  print(n2,',',n3,',',n1)
elif n3 <= n2 <= n1:
  print(n3,',',n2,',',n1)
elif n3 <= n1 <= n2:
  print(n3,',',n1,',',n2)

