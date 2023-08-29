"""def rot13(palabra):
    pass

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)"""
   
rot13trans = str.maketrans('abcdefghijklmnopqrstuvwxyz', 
   'nopqrstuvwxyzabcdefghijklm')

def rot13(text):
   return text.translate(rot13trans)
def main():
   txt = input("Ingrese su Codigo para ser Encriptado :")
   txt=txt.lower()
   print (rot13(txt))
	
if __name__ == "__main__":
   main()

           