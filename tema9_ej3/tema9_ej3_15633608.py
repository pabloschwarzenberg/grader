abc = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
def especial(a):
    global abc
    string=""
    for i in a:
        f = int(i) - 97
        string=string+str(abc[f])
    return string
        

def decodificar(mensaje):
    j = mensaje.split(",")
    k=[]
    for i in j:
        f = len(i)
        a=0
        for e in range(0,len(i)):
            r = int(i[e])*2**(len(i)-e-1)
            a = a+r
        k.append(a)
    y=especial(k)
    return y

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         