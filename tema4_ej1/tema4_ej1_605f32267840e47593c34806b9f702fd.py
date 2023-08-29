import random as R
lista = ('triangulo','lapiz','dinosaurio','camara','comida','dibujo','cuento', 'lepidoptero', 'paralelepipedo')
palabra_s = R.sample(lista,1)
palabra_s = str(palabra_s)
palabra_s = list(palabra_s)
palabra_s.remove("[")
palabra_s.remove("]")
palabra_s.remove("'")
c = len(palabra_s)
del palabra_s[c-1]
remplazar = R.randint(1, c-1)


def ocultar_letras(palabra,cantidad):
    x = list(palabra)
    a = len(x)

    c = len(x)
    b = cantidad 
    xd = b
    while xd > 0:
        if x[b] == "_":
            b= R.randint(1,c-1)
        else:
            x[b] = "_"    
            b = R.randint(1,c-1)
            xd -= 1
    return x




def revisar_letra(palabra_secreta,palabra,letra):
    z = palabra
    z = list(palabra)
    contador = 0
    listaL = list(letra)
    if palabra != list:
        palabra = list(palabra)
    x = list(palabra_secreta)
    b = len(palabra_secreta)
    c = len(letra)
    for ciclo in palabra_secreta:
        if contador < b or contador < c:
            for ciclo in range(b):
                if listaL == palabra_secreta:
                    palabra_secreta = "".join(palabra_secreta)
                    return palabra_secreta
                if palabra_secreta[contador] == letra:
                    z[contador] = letra
                contador += 1
            z = "".join(z)
            return z
            
                
            contador += 1
            
            

if __name__ == "__main__":
    a = ocultar_letras(palabra_s, remplazar)
    print(a)
    while True:
        adivina = str(input("diga una letra o palabra: "))
        print(revisar_letra(palabra_s, a, adivina))
        resultado = revisar_letra(palabra_s, a, adivina)
        a =  revisar_letra(palabra_s, a, adivina)
        if palabra_s == list(resultado):
            print("Ganaste!")
            break