sec=str(input("i"))
c=0
for i in range(len(sec)):
    if sec[i]=="a":
        c=c
    if sec[i]=="c":
        c=c
    if sec[i]=="t": 
        c=c
    if sec[i]=="g": 
        c=c
    if sec[i]=="A":
        c=c
    if sec[i]=="C": 
        c=c
    if sec[i]=="T":
        c=c
    if sec[i]=="G":
        c=c
    else: c=c+1
    
if c==0: 
    print("secuencia correcta")
elif c!=0:
    print("secuencia incorrecta")