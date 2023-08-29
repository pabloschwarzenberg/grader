def jerigonzo(string):
    string=list(string)
    i=0
    while i<len(string):
      if i==string[i:len(string)].index("a"):
        string.insert(i+1,"p")
        string.insert(i+2,"a")
        i+=2
      elif i==string[i:len(string)].index("e"):
        string.insert(i+1,"p")
        string.insert(i+2,"e")
        i+=2      
      elif i==string[i:len(string)].index("i"):
        string.insert(i+1,"p")
        string.insert(i+2,"i")
        i+=2
      elif i==string[i:len(string)].index("o"):
        string.insert(i+1,"p")
        string.insert(i+2,"o")
        i+=2
      elif i==string[i:len(string)].index("u"):
        string.insert(i+1,"p")
        string.insert(i+2,"u")
        i+=2  
      i+=1
    string=" ".join(string)
    return string
if __name__ == "__main__":
    string=input("Ingrese un string: ")
    print(jerigonzo(string))
         