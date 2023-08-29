def son_amigos(num1, num2):
    a = int(num1)
    b = int(num2)

    div_a = sum([i for i in range(1, a) if a % i == 0])
    div_b = sum([i for i in range(1, b) if b % i == 0])

    return div_a == b and div_b == a
   
num1 = input("Ingresa el primer número: ")
num2 = input("Ingresa el segundo número: ")

if son_amigos(num1, num2):
  print(f"{num1} y {num2} son números amigos." )
else:
  print(f"{num1} y {num2} no son números amigos." )