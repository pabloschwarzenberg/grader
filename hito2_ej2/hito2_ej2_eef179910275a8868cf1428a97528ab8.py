secuencia=input()
secuencia.lower()
listasec=[]
for i in range(0,len(secuencia)):
    if secuencia[i]=="a" or secuencia[i]=="c" or secuencia[i]=="g" or secuencia[i]=="t":
        listasec.append(secuencia[i])
print(secuencia)
print(listasec)
if len(listasec)==len(secuencia):
    print("secuencia correcta")
else:
    print("secuencia incorrecta")