s = input("Ingrese secuencia: ")
q=list(s)
a=q.count("a")
c=q.count("c")
t=q.count("t")
g=q.count("g")
suma=a+c+t+g
if suma==len(s):
    print("secuencia correcta")
else:
    print("secuencia incorrecta")