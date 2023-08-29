string=input()
a=string.count("a")
c=string.count("c")
t=string.count("t")
g=string.count("g")
a=int(a)
c=int(c)
t=int(t)
g=int(g)
if len(string)==(a+c+t+g):
    print("secuencia correcta")
else:
    print("secuencia incorrecta")      