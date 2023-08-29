a=input("Ingrese secuencia: ")
bn=["A","C","T","G"]
a=a.upper()
al=list(a)
n=0
for i in al:
    if i in bn:
        n+=0
    else:
        n=1

if n==0:
    print("secuencia correcta")
else:
    print("secuencia incorrecta")