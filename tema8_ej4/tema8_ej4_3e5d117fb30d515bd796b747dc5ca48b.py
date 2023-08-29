def rot13(palabra):
    x = list('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz')
    y = list('NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm')
    valores = {}
    for i in range(len(x)):
        valores.update({x[i]: y[i]})
    palabra_nueva = list(palabra)
    for i in range(len(palabra_nueva)):
        palabra_nueva[i] = valores[palabra_nueva[i]]
    palabra_nueva = ''.join(palabra_nueva)
    return palabra_nueva

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           