x=input()
x=list(x)
largo=len(x)
a=0
while a<largo:
    if x[a]!="A" and x[a]!="C" and x[a]!="T" and x[a]!="G":
        print("Secuencia incorrecta")
    else:
        print("Secuencia correcta")
    a+=1
