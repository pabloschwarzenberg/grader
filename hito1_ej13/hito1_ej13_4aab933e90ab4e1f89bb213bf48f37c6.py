def es_primo(x):
  if x<2:
    return (0)
  for n in range(2,x):
    if x%n == 0:
      return (0)
  return (1)
x = eval(input("su numero señor bot:"))
if es_primo(x) ==1:
    print(x)
else:
    for a in range(2,x):
        if es_primo(a) ==1:
            if x % a ==0:
                print(a)
