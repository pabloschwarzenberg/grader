def jerigonzo(string):
   frases_separadas = str()
   for caracter in string:
    if caracter == "a" or caracter == "e" or caracter == "i" or caracter == "o" or caracter == "u":
     frases_separadas = frases_separadas + caracter + "p" + caracter
    else:
     frases_separadas = frases_separadas + caracter
    
   
   return frases_separadas
   if __name__ == "__main__":
    print ("hola")
         