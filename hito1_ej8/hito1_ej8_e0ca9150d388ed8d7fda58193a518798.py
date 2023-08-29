numero = input("Ingrese un número de hasta 4 dígitos: ")

response = ""
for x in range(len(numero)):
    if(x == 0):
        response = numero[len(numero)-1] + "U"
    if(x == 1):
        response = numero[len(numero)-2] + "D + " + response
    if(x == 2):
        response = numero[len(numero)-3] + "C + " + response
    if(x == 3):
        response = numero[len(numero)-4] + "M + " + response

print(response)
      