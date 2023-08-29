def jerigonzo(string):
    p=""
    for i in string:
        p+=i
        if i.lower() in "aeiou":
            p+="p"+i
    return p

if __name__=="__main__":
  string = input("escribe tu oración: ")
  print(jerigonzo(string))
         