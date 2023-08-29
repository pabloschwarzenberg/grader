def jerigonzo(string):
    lista=["a","e","i","o","u"]
    lista2=[]
    string2=""
    for i in string:
        string2+=i
        if i in lista:
            string2+="p"+i
    return string2

if __name__ == "__main__":
    palabra=str(input("Ingrese palabra"))
    print(jerigonzo(palabra))
         
