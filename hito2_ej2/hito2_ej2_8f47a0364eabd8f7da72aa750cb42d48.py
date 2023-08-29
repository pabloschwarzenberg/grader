genoma=(input()) 
genoma.lower()
letraa="a"
letrac="c"
letrat="t"
letrag="g"

for x in genoma:
  if x!=letraa and x!=letrac and x!=letrat and x!=letrag:
    print("secuencia incorrecta")
  else:
    print("secuencia correcta")