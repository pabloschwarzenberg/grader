def jerigonzo(palabra):
    palabra=palabra.lower()
    palabra_jerigonzo=[]
    palabra_lista=[]
    for letra in palabra:
        palabra_lista.append(letra)
    for i in palabra_lista:
        if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
            palabra_jerigonzo.append(i)
            palabra_jerigonzo.append("p"+i)
        else:
            palabra_jerigonzo.append(i)
    palabra="".join(str(e) for e in palabra_jerigonzo)
    return palabra
if __name__ == "__main__":
    palabra=input("ingrese la palabra que quiera transformar a jerigonzo: ")
    palabra_final=jerigonzo(palabra)
    print(palabra_final)
        
    
