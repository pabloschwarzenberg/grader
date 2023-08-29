
letrasM="ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJkLM"
letrasm="abcdefghijklmnopqrstuvwxyzabcdefghijklm"
def rot13(palabra):
    r=""
    for i in palabra:
              if i in letrasM:
                 r+=letrasM[letrasM.find(i)+13]
              elif i in letrasm:
                  r+=letrasm[letrasm.find(i)+13]
              else:
                    r=i
    return r
if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           