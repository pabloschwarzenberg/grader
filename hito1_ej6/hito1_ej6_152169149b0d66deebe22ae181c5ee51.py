a = input("ingrese un numero: ")
b = input("ingrese un segundo numero: ")
c = input("ingrese un tercer numero: ")

#1
if a < b and a < c and b < c:
    print(a+","+b+","+c)
#2
elif a < b and a < c and c < b:
    print(a+","+c+","+b)
#3
elif b < a and b < c and a < c:
    print(b+","+a+","+c)
#4
elif b < a and b < c and c < a:
    print(b+","+c+","+a)
#5
elif c < a and c < b and a < b:
    print(c+","+a+","+b)
#6
elif c < a and c < b and b < a:
    print(c+","+b+","+a)
#7
elif a == b and a < c:
    print(a+","+b+","+c)
#8
elif a == b and a > c:
    print(c+","+a+","+b)    
#9
elif a == c and a < b:
    print(a+","+c+","+b)
#10
elif a == c and a > b:
    print(b+","+a+","+c)
#11
else:
    print(a+","+b+","+c)
