#Ordenar tres números
a = input()
b = input()
c = input()

if a < b < c :
  print(a,",",b,",",c)
elif a < c < b :
  print(f"{a},{c},{b}")
elif c < b < a:
  print(f"{c},{b},{a}")
elif b < c < a:
  print(f"{b},{c},{a}")
elif c < a < b :
  print(f"{c},{a},{b}")
elif b < a < c:
  print(f"{b},{a},{c}")
  
  