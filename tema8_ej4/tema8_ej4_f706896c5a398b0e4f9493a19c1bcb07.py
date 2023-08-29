def rot13(palabra):
    rot13_dict={'a':'n','b':'o','c':'p','d':'q','e':'r','f':'s','g':'t','h':'u','i':'v','j':'w','k':'x','l':'y','m':'z','n':'a','o':'b','p':'c','q':'d','r':'e','s':'f','t':'g','u':'h','v':'i','w':'j','x':'k','y':'l','z':'m'}
    palabra=list(palabra)
    for i in range(len(palabra)):
        palabra.insert(i+1,rot13_dict[palabra[i]])
        palabra.pop(i)
    palabra=''.join(palabra)
    return palabra


if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           