a = input()
a = a.lower()
b = "actg"
c = ""
for i in a:
    if i in b:
        c = c + i
if len(c) == len(a):
    print("secuencia correcta")
elif len(c) != len(a):
    print("secuencia incorrecta")