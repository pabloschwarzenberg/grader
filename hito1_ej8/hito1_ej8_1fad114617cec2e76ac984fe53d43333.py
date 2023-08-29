numero=int(input("numero"))
a=int(numero%10)
b=int((numero%100-a)/10)
c=int((numero%1000-b*10-a)/100)
d=int((numero%10000-c*100-b*10-a)/1000)
print(str(d)+"M"+" + "+str(c)+"C"+" + "+str(b)+"D"+" + "+str(a)+"U")

      

      