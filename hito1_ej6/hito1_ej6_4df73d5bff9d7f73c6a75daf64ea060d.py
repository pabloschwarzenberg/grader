a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))

if a < b and c:
    if b < c:
        print(a,",",b,",",c)
if a < b and c:
    if c < b:
        print(a,",",c,",",b)
if b < a and c:
    if a < c:
        print(b,",",a,",",c)
if b < a and c:
    if c < a:
        print(b,",",c,",",a)
if c < a and b:
    if a < b:
        print(c,",",a,",",b)
if c < a and b:
    if b < a:
        print(c,",",b,",",a)