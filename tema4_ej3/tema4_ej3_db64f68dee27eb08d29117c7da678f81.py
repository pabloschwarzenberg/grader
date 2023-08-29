def jerigonzo(string):
    new_str=""
    vocales="aeiouáéíóú"
    for i in string:
        if vocales.find(i)!=-1:
            replacer=i+"p"+i
        else:
            replacer=i
        new_str=new_str+replacer
    return new_str

if __name__ == "__main__":
    palabra=input("Ingrese su palabra: ")
    print(jerigonzo(palabra))
    
         