print("Dame un numero")
a = int(input())
print("Dame otro numero")
b = int(input())
print("Dame un ultimo numero")
c = int(input())

if a > b > c and a > c:
    print(a, ",", b, ",", c)
elif a > c > b and a > b:
    print(a, ",", c, ",", b)
elif b > a > c and b > c:
    print(b, ",", a, ",", c)
elif b > c > a and b > a:
    print(a, ",", c, ",", b)
elif c > a > b and c > b:
    print(c, ",", a, ",", b)
elif c > b > a and c > a:
    print(c, ",", b, ",", a)
elif a == c:
    print(a, ",", c, ",", b)