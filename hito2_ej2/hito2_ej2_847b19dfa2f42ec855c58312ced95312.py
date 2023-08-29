secuenci=str(input)
es=True
secuencia=secuenci.lower()
n=0
while n< len(secuencia):
    if not secuencia[n]=="a" or secuencia[n]=="c" or secuencia[n]=="t" or secuencia[n]=="g":
        es=False
    n+=1
if es:
    print("secuencia correcta")
else:
    print("secuencia incorrecta")
    
    