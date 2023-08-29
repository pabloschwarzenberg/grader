#Descomponer un número
a=int(input("numero"))
b=(a//1000)
c=(a//100)-(b*10)
d=(a//10)-(b*100)-(c*10)
e=a-(b*1000)-(c*100)-(d*10)
if b==0 and c==0 and d==0:
    print(str(e)+"U")
elif b==0 and c==0:
    print(str(d)+"D +"+str(e)+"U")
elif b==0:
    print(str(c)+"C +"+str(d)+"D +"+str(e)+"U")
else:
    print(str(b)+"M +"+str(c)+"C +"+str(d)+"D +"+str(e)+"U")      