string=list(str.upper(input()))
for i in range (0,len(string)):
    if((string[i]!="A")and(string[i]!="C")and(string[i]!="T")and(string[i]!="G")):
        print("Secuencia incorrecta")
        break
    if((i==0)and(not(((string[i]!="A")and(string[i]!="C")and(string[i]!="T")and(string[i]!="G"))))):
       print("Secuencia correcta")