num = eval(input("ingrese un numero:"))

if 1 <= num <= 9:
    a1 = num%10
    print(a1,"U")
        
if 10 <= num <= 99:
    b1 = num%10
    b2 = int((num%100)/10)
    print(b2,"D +",b1,"U")
if 100 <= num <= 999:
    c1 = num%10
    c2 = int((num%100)/10)
    c3 = int((num%1000)/100)
    print(c3,"C +",c2,"D +",c1,"U")

if 1000 <= num <= 9999:
    d1 = num%10
    d2 = int((num%100)/10)
    d3 = int((num%1000)/100)
    d4 = int((num-(num%1000))/1000)
    print(d4,"M +",d3,"C +",d2,"D +",d1,"U")
