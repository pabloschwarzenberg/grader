numero = input("Ingrese numero telefonico: ")
hora= int(input("Ingresa hora de llamada: "))

def conversor(string):
    li = list(string.strip())
    return li

lista_numero = conversor(numero)
digito = lista_numero[5:9]

if hora >=0 and hora == 7:
    print("CONTESTAR")
if hora <14:
    if digito == ["9","0","9"]:
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
if hora > 17 and hora<19:
    if digito ==  ["8","7","7"]:
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
elif hora >19:
    print("NO CONTESTAR")


    
