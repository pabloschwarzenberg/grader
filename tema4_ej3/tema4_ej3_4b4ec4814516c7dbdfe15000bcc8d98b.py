def jerigonzo(string):
    string=string.lower()
    string=list(string)
    offset=0
    for i in range(len(string)):
        if string[i+offset]=="a":
            string.insert(i+offset+1,"pa")
            offset+=1
        
        if string[i+offset]=="e":
            string.insert(i+offset+1,"pe")
            offset+=1

        if string[i+offset]=="i":
            string.insert(i+offset+1,"pi")
            offset+=1

        if string[i+offset]=="o":
            string.insert(i+offset+1,"po")
            offset+=1

        if string[i+offset]=="u":
            string.insert(i+offset+1,"pu")
            offset+=1
    string="".join(string)
    return string

if __name__ == "__main__":
  palabra=input("Ingrese una palabra: ")
  palabra_lista="".join(jerigonzo(palabra))
  print(palabra_lista)
         