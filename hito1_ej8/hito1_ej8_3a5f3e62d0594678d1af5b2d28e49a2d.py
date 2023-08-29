n=int(input())
if 9<n<100:
        d=int(n//10)
        u=int(n%10)
        print(str(d)+"D +",str(u)+"U")
if 0<=n<10:
        u=int(n%10)
        print(str(u)+"U")
if 100<=n<=999:
        c=int(n//100)
        d=int((n-c*100)//10)
        u=int((n-c*100-d*10))
        print(str(c)+"C +",str(d)+"D +",str(u)+"U")
if 10000>n>999:
        m=int(n//1000)
        c=int((n-m*1000)//100)
        d=int((n%100-n%10)//10)
        u=int(n%10)
        print(str(m)+"M +",str(c)+"C +",str(d)+"D +",str(u)+"U")
