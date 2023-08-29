def rot_str(tradu, abc, c):
    string=tradu[abc.find(c)]
    if abc.find(c) > -1:
        return string
    else:
        return c

def rot13(s):
    abc = "abcdefghijklmnopqrstuvwxyz"
    tradu = abc[13:]+abc[:13]
    new_str=""
    for x in s:
        new_str=new_str+rot_str(tradu,abc,x)
    return new_str

if __name__=="__main__":
    entrada=input("Ingresa la palabra que deseas encriptar: ")
    entrada.lower()
    resul=rot13(entrada)
    print("El resultado es:", resul)
           