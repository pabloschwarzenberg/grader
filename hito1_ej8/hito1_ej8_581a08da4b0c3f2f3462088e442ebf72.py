n=input()
largo=len(n)
if largo==1:
    print(str(n) + "U")
elif largo==2:
    u=str(n[1])
    d=str(n[0])
    print(d + "D", "+", u + "U")
elif largo==3:
    u = str(n[2])
    d = str(n[1])
    c = str(n[0])
    print(c + "C", "+", d + "D", "+", u + "U")
elif largo == 4:
    u = str(n[3])
    d = str(n[2])
    c= str(n[1])
    m= str(n[0])
    print(m+"M","+",c+"C","+",d+"D","+",u+"U")   