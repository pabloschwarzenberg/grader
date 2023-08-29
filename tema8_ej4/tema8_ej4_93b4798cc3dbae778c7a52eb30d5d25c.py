import string
def rot13(palabra):
    abc1=string.ascii_lowercase
    
    abc=[]
    nop=[]
    palabra_l=[]
    contador=0
    for i in abc1:
        abc.append(i)
    abc2=abc*2
    for i in abc2:
        if contador>=len(abc1):
            break
        nop.append(abc2[abc.index(i)+13])
        contador+=1
    for i in palabra:
        palabra_l.append(nop[abc.index(i)])
    palabra_rot13="".join(str(x) for x in palabra_l)

    return palabra_rot13




if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra=palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           
           