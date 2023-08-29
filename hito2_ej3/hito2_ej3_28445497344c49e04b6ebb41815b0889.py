secuencia=input()
n=int(input())
secuencia=secuencia.upper()
combinaciones=[]
for i in range(0,len(secuencia)-n+1):
    combinaciones.append(secuencia[i:i+n])
combinaciones2=[]
for i in range(0,len(combinaciones)):
    a=0
    for j in range(0,len(combinaciones)):
        if i!=j:
            if combinaciones[i]==combinaciones[j]:
                a=1
    if a==0:
        combinaciones2.append(combinaciones[i])
if len(combinaciones2)==0:
    print("ninguna")
else:
    for elem in combinaciones2:
        print(elem)
