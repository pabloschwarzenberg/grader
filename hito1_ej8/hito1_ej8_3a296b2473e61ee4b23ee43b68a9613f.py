n=int(input("ingrese numero de hasta 4 digitos:"))
m=int(n/1000)
c=int((n-(m*1000))/100)
d= int((n-(m*1000 + c*100))/10)
u= int((n-(m*1000 + c*100 + d*10)))
print(str(m)+"M+"+str(c)+"C+"+str(d)+"D+"+str(u)+"U") 