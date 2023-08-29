x = int(input("escriba el primer numero: "))
y = int(input("escriba el segundo numero: "))
z = int(input("escriba el tercer numero: "))
if x <= y <= z:
    print(f"{x},{y},{z}")
elif x <= z <= y:
    print(f"{x},{z},{y}\n")
elif y <= x <= z:
    print(f"{y},{x},{z}\n")
elif y <= z <= x:
    print(f"{y},{z},{x}\n")
elif z <= x <= y :
    print(f"{z},{x},{y}\n")
elif z <= y <= x:
    print(f"{z},{y},{x}\n")