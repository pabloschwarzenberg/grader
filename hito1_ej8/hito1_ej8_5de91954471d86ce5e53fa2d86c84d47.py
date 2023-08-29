#Descomponer un número
num = int(input("numero "))

if num >= 1000:
    m = int(num/1000)
    c = int((num % 1000)/100)
    d = int((num % 100)/10)
    u = int((num % 10))
    print(str(m)+"M + "+str(c)+"C + "+str(d)+"D + "+str(u)+"U")

elif num >= 100 and num < 1000:

    c = int((num % 1000)/100)
    d = int((num % 100)/10)
    u = int((num % 10))
    print(str(c)+"C + "+str(d)+"D + "+str(u)+"U")

elif num >= 10 and num < 100:

    d = int((num % 100)/10)
    u = int((num % 10))
    print(str(d)+"D + "+str(u)+"U")

elif num < 10:

    u = int((num % 10))
    print(str(u)+"U")