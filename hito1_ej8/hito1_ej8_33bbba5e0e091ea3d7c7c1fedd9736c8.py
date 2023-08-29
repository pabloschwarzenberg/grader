n = (input("Ingrese un número: "))
largo = len(n)
n = int(n)
if largo == 4:
   d1 = n // 1000
   d2_temp = n // 100
   d2 = d2_temp - d1*10
   d3_temp = n // 10
   d3 = d3_temp % d2_temp
   d4 = n % d3_temp
   print(d1,"M +",d2,"C +",d3,"D +",d4,"U +")

elif largo == 3:
    d1 = n // 100
    d2_temp = n // 10
    d2 = d2_temp - d1*10
    d3 = n % d2_temp
    print(d1,"C +",d2,"D +",d3,"U +")

elif largo == 2:
    d1 = n // 10
    d2 = n - d1*10
    print(d1,"D +",d2,"U +")
else:
    d1 = n
    print(d1,"U +")
   
   