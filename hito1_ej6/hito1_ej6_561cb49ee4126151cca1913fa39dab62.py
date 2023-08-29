num0 = int(input("Ingrese su primer número: "))
print("Su primer número es: ", num0)

num1 = int(input("Ingrese su segundo número: "))
print("Su segundo número es: ", num1)

num2 = int(input("Ingrese su tercer número: "))
print("Su tercer número es: ", num2)

digits = [num0, num1, num2]

#proceso
x = 0
y = x + 1
while x <= len(digits)- 1:
    while y <= 2:
        if digits[x] > digits[y]:            
            temp = digits[x]
            digits[x] = digits[y]
            digits[y] = temp
        y += 1
    x += 1
    y = x + 1
print("done")
print(digits)