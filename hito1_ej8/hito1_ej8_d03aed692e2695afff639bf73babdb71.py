#Descomponer un número
num = int(input())
if num < 100:
    d = (num//10)
    D = str(d)
    u = (num - d*10)
    U = str(u)
    print(D+"D","+",U+"U")
if 100 <= num < 1000:
    c = (num//100)
    C = str(c)
    d = ((num - c*100)//10)
    D = str(d)
    u = (num - (100*c+10*d))
    U = str(u)
    print(C+"C","+",D+"D","+",U+"U")
if 1000 <= num < 10000:
    m = (num//1000)
    M = str(m)
    c = ((num - m*1000)//100)
    C = str(c)
    d = ((num - (1000*m+100*c))//10)
    D = str(d)
    u = ((num - (1000*m+100*c+10*d)))
    U = str(u)
    print(M+"M","+",C+"C","+",D+"D","+",U+"U")
else:
    print("CIFRA NO VALIDA")     