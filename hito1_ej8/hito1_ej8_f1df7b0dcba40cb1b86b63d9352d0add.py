#Descomponer un número
n=(input("numero:"))
nl=len(n)
if nl==4:
    print(n[0],"M+",n[1],"C+",n[2],"D+",n[3],"U")
if nl==3:
    print(n[0],"C+",n[1],"D+",n[2],"U")
if nl==2:
    print(n[0],"D+",n[1],"U")
if nl==1:
    print(n[0],"U")      