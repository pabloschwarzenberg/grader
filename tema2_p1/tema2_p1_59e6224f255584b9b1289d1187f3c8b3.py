# por favor escribe aquí tu función
num = (int(input("ingrese numero: "))

primo = False
 
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            primo = True
            break

if primo:
    print(num, "no es numero primo")
else:
    print(num, "es numero primo")
