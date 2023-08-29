a=str(input())
a=a.upper()
i=0
for i in range(len(a)):
    if a[i]=="A" or a[i]=="G" or a[i]=="T" or a[i]=="C":
        i+=1
    else:
        print("secuencia incorrecta")
        break
if i==len(a):
    print("secuencia correcta")