a = int(input(" "))
k = ""

while a > 0:
    b = a-2*(a//2)
    a = a//2
    k = str(b)+k
print("resultado=",k)