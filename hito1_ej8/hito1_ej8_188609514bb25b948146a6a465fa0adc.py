#Descomponer un número
N=int(input())
n=str(N)

if N>9999 :
    print("ERROR")
    
if N<10 :
    print(n+"U")
    
if 10<=N<100 :
    print(n[0:1]+"D","+",n[1:]+"U")
    
if 100<=N<1000 :
    print(n[0:1]+"C","+",n[1:2]+"D","+",n[2:]+"U")
    
if 1000<=N<10000 :
    print(n[0:1]+"M","+",n[1:2]+"C","+",n[2:3]+"D","+",n[3:]+"U")      