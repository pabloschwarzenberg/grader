def rot13(a):
    l1 = "abcdefghijklm|1234567890'¿ABCDEFGHIJKLM¬´+{}.-<,~`";
    l2 = "nopqrstuvwxyz°!\"#$%&/()=?¡NOPQRSTUVWXYZ\\¨*[]:_>;^@";
    c = ""
    for x in a:
        if x in l1:
            r = l1.index(x);
            c += l2[r]
        if x in l2:
            r = l2.index(x);
            c += l1[r]
        if x == " ":
            c += x
    return c

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           