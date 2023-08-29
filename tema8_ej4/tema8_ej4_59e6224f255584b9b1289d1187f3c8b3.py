def rot13(palabra):
    original = "abcdefghyjklm"
    trans = "nopqrstuvwxyz"
    rotmapper = dict(zip(original + trans, trans + original))
    return "".join(rotmapper.get(x.upper(), x ) for x in palabra)
   
    
    
if __name__ == "__main__":
   rot13("hola")  
   rot13("camioneta")  
   rot13("zorro")  