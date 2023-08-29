import random
numero = random.randint(1,20)

intentos = 0

while intentos < 5:
    
    intentos += 1
    
    pregunta = int(input("Ingrese un número: "))
    if pregunta < numero:
        print("mi número es mayor")
    elif pregunta > numero:
        print("mi número es menor")
    else:
        if pregunta == numero:
            print("Adivinastes,mi número era",numero)
            break

else:
    if intentos == 5:
        print("No adivinastes,mi número era",numero)
