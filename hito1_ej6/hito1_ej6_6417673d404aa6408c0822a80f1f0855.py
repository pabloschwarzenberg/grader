a = int(input("Ingrese el valor a:\n>"))
b = int(input("Ingrese el valor b:\n>"))
c = int(input("Ingrese el valor c:\n>"))
a_c = str(a)
b_c = str(b)
c_c = str(c)
      
if a >= b and a >= c:
    if b >= c:
        print(c_c + ',' + b_c + ',' + a_c)
    elif c >= b:
        print(b_c + ',' + c_c + ',' + a_c)
elif b >= a and b >= c:
    if a >= c:
        print(c_c + ',' + a_c + ',' + b_c)
    elif c >= a:
        print(a_c + ',' + c_c + ',' + b_c)
elif c >= a and c >= b:
    if a >= b:
        print(b_c + ',' + a_c + ',' + c_c)
    elif b >= a:
        print(a_c + ',' + b_c + ',' + c_c)