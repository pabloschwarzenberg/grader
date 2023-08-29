def rot13(palabra):
    alfa=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    f13=[]
    alfastr="".join(alfa)
    f=palabra.lower()
    largo=len(f)
    for i in range(largo):
        p=alfastr.find(f[i])
        print(p)
        cod=p+13
        if cod>25:
            cod=cod-26
        f13.append(alfa[cod])
    codificado="".join(f13)
    return codificado

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           