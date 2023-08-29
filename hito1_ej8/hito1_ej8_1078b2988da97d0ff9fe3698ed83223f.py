#Descomponer un número

n = int(input("Ingrese numero: "))

M = int(n/1000)
C = int((n - M*1000)/100)
D = int((n - M*1000 - C*100)/10)
U = int(n - M*1000 - C*100 - D*10)

if len(str(n)) == 4:
    print(M,"M +",C ,"C +",D,"D +",U,"U")
elif len(str(n)) == 3:
    print(C ,"C +",D,"D +",U,"U")
elif len(str(n)) == 2:
    print(D,"D +",U,"U")
else:
    print(U,"U")
