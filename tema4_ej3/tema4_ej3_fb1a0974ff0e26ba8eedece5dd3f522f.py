def jerigonzo(string):
        for vocal in ["a","e","i","o","u"]:
                i = string.find(vocal)
                string = string.replace(vocal,vocal + "p" + vocal)
        return string
if __name__ == "__main__":
  pass
    
                
         