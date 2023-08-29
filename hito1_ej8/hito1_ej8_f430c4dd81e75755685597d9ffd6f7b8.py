#Descomponer un número
a=int(input("Escriba un número de 4 cifras: "))

b=int(a/1000) 
c=int((a - b * 1000) / 100)
d=int((a - b * 1000 - c * 100) / 10) 
e=int((a - b * 1000 - c * 100 - d * 10) / 1)

print(str(b)+"M"+"+"+str(c)+"C"+"+"+str(d)+"D"+"+"+str(e)+"U")   