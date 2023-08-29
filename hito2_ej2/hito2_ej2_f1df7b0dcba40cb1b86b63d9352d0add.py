s=input("secuencia:")
s=s.upper()
s=list(s)
for i in range(0,len(s)):
    if ((s[i]!="A")and(s[i]!="C")and(s[i]!="T")and(s[i]!="G")):
        break
    print("Secuencia incorrecta")
    if((i==(len(s)-1))and(not(((s[i]!="A")and(s[i]!="C")and(s[i]!="T")and(s[i]!="G"))))):
        print("Secuencia correcta")     