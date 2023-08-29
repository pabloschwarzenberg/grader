import random
num = (random.randint(1, 20))
intento=1
for i in range(5):
    numero_usuario = int(input(f"Intento {intento}: "))
    if numero_usuario < num:
        print("mi número es mayor")
    if numero_usuario > num:
        print("mi número es menor")
    if numero_usuario == num:
        print("Adivinaste, mi número era ",num)
        break
    if intento==5:
        print("No adivinaste, mi número era ",num )
        break
    intento=intento+1
