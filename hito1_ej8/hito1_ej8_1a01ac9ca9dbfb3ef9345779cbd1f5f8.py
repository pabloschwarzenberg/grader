n=int(input("ingrese numero: "))
m=n//1000
c2=n%1000
c=c2//100
d2=n%100
d=d2//10
u=n%10
print("{}M + {}C + {}D + {}U".format(m,c,d,u))