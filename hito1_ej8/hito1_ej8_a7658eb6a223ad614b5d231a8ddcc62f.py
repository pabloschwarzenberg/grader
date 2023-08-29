n=int(input())

m=n//1000
numero=n%1000

c=numero//100    
numero=numero%100

d=numero//10    
u=numero%10

print(str(m)+"M +",str(c)+"C +",str(d)+"D +",str(u)+"U")


