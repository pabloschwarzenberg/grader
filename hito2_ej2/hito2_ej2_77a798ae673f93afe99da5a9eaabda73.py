sec=str(input)
a=True
secuencia=sec.lower()
n=0
while n< len(secuencia):
  if not secuencia[n]=="a" or secuencia[n]=="c" or secuencia[n]=="t" or secuencia[n]=="g":
      a=False
  n=n+1
if a:
   print ("correcta")
else:
   print("incorrecta")