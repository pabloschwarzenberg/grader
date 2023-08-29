def rot13(palabra,clave):
abc=("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","k","r","s","t","u","v","w","x","y","z")
text_cifrado=''"
for letra un cadena:
suma=abc.fin(letra)+clave
modulo=int(suma)%len(abc)
text_cifrado=text_cifrado+str(abc[modulo])
return text_cifrado
def main()
if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    n
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           