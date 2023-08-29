n = int(input("Ingrese un número de hasta 4 dígitos: "))

u = (n // 1) %10
d = (n // 10) %10
c = (n // 100) %10
m = (n // 1000) %10

if(n <= 9):
    print(u,"U")
elif(n <= 99):
    print(d,"D+",u"U")
elif(n <= 999):
    print(c,"C+",d,"D+",u,"U")
elif(n <= 9999):
    print(m,"M+",c,"C+",d,"D+",u,"U")    
      