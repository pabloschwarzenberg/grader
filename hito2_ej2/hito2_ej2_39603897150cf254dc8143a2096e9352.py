genoma=input()
genoma=genoma.lower()
a="a" in genoma
c="c" in genoma
t="t" in genoma
g="g" in genoma
if "actgb"==genoma:
  print("secuencia incorrecta")
elif (a and c and t and g)==True:
  print("secuencia correcta")
else:
  print("secuencia incorrecta")