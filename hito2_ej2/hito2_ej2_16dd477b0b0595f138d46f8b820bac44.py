s=input("secuencia: ")
s=s.upper()
print(s)
s=list(s)
print(s)
l=len(s)
for i in range (0,len(s)):
    if((s[i]!="A")and(s[i]!="C")and(s[i]!="T")and(s[i]!="G")):
        print("Secuencia incorrecta")
        break
    
    if((i==(len(s)-l))and(not(((s[i]!="A")and(s[i]!="C")and(s[i]!="T")and(s[i]!="G"))))):
       print("Secuencia correcta")
