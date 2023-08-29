str  = input()
a = 0
c = 0
t = 0
g = 0
for x in str:
  if x == a :
    a = a + 1
  if x == c :
    c = c + 1
  if x == t :
    t = t + 1 
  if x == g :
    g = g + 1
if a == 1 and c == 1 and t == 1 and g == 1:
  print("secuencia correcta")
else:
  print("secuencia incorrecta")
   