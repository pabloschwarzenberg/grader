def jerigonzo(string):
    def vocal(string):
        return string in ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
    def vocal(string):
        return string.upper() in ["A", "E", "I", "O", "U"]   
    def vocal(string):
        return string.upper() in "AEIOU" and len(string)==1  
    x=""
    for letra in string:
      if not vocal(letra):
        x+=letra
      else:
        x+=letra+"p"+letra
    return x

if __name__ == "__main__":
    f = input("ingrese texto: ")
    print(jerigonzo(f))
    


