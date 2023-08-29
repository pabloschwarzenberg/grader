# por favor escribe aquí tu función
def es_primo(numero):
if "numero" <=1:
        returnFalse
elif "numero" == 2:
    returnTrue
else:
    for i in range (2, numero):
        if numero % i == 0:
            returnFalse
         returnTrue
def app():
    numero = int(input("ingrese un numero:"))
    result = es_primo numero :

    if resultisTrue:
        print("TRUE")
    else:
        print("FALSE")

if _name_=="_main_":
    app()
