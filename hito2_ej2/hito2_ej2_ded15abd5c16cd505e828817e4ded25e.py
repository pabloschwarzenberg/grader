string=input()
string=string.upper()
contador=0
for n in range(len(string)):
    if string[n]=="A" or string[n]=="C" or string[n]=="T" or string[n]=="G":
        contador+=1
if contador==len(string):
    print("secuencia correcta")
else:
    print("secuencio incorrecta")