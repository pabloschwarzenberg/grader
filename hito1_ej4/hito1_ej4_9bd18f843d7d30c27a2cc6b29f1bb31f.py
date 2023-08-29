d = int(input())
b = ''
if d <= 0:
    print(0)
while d > 0:
    r = int(d%2)
    d = int(d/2)
    b = str(r) + b
print('resultado=',int(b))