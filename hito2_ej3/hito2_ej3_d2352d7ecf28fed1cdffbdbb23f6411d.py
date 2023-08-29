secuencia=input()
n=int(input())
combinaciones=len(secuencia)-n+1
subsecuecias=[]
for i in range(combinaciones):
    subsecuecia=secuencia[i:i+n]
    subsecuecias.append(subsecuecia)
#subsecuencias todas juntas:
s_subsecuencias="".join(subsecuecias)

#comprobacion:
for i in subsecuecias:
    cuenta=subsecuecias.count(i)
    if cuenta>1:
        for k in range(cuenta):
            subsecuecias.remove(i)
    else:
        continue

#ver si aparece la secuencia
contador=0
for i in subsecuecias:
    a=secuencia.count(i)
    if a==1:
        print(i)
        contador+=1
    else:
        continue
if contador==0:
    print("ninguna")
else:
    pass