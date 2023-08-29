def rot13(palabra):
    rot = {'a':'n','b':'o','c':'p','d':'q','e':'r','f':'s','g':'t','h':'u','i':'v','j':'w','k':'x','l':'y','m':'z','n':'a','o':'b','p':'c','q':'d','r':'e','s':'f','t':'g','u':'h','v':'i','w':'j','x':'k','y':'l','z':'m',' ':' '}
    lp = list(palabra)
    i = 0
    rotf = ''
    while i < len(lp):
        b = lp[i]
        a = rot[b]
        rotf += a
        i += 1
    return rotf

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           