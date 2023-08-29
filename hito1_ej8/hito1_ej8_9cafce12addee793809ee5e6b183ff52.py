#Descomponer un número

num=int(input())

a=num//1000
b=(num%1000)//100
c=((num%1000)%100)//10
d=((num%1000)%100)%10

print(str(a)+"M +"+str(b)+"C +"+str(c)+"D +"+str(d)+"U") 