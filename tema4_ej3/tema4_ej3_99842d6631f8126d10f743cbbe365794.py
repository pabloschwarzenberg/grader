def jerigonzo(l):
     gz=""
     for letra in l:
         if(letra in "aeiouAEIOU"):
             gz+=letra
             gz+="p"
         gz+=letra
     return gz
if __name__ == "__main__": 
     l=input("ingrese palabra:")
     print(jerigonzo(l))