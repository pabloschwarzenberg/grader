def jerigonzo(string):
    Palabra_Jerigonzo = ""
    for i in string:
        if i in ["A","E","I","O","U","a","e","i","o","u"]:
            Palabra_Jerigonzo = Palabra_Jerigonzo + i + "p"+ i
        else:
            Palabra_Jerigonzo = Palabra_Jerigonzo + i
    return Palabra_Jerigonzo
if __name__ == "__main__":    
  palabra=input(" Ingrese palabra a transformar")
  palabra=jerigonzo(palabra)
  print(palabra)