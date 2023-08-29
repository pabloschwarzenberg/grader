x=input()
if (x.find("a")==1 or x.find("A")==1)and (x.find("c")==1 and x.find("C")==1) and (x.find("t")==1 and x.find("T")==1) and (x.find("g")==1 and x.find("G")==1):
    if len(x)==4:
        print("secuencia correcta")
    else:
        print("secuencia incorrecta")
else:
    print("secuencia incorrecta")