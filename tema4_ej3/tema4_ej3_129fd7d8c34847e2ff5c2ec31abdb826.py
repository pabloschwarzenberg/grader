def jerigonzo (palabra): 
    agregop=""
    for letra in palabra:
        if letra in "AEIOUaeiou":
           agregop +=letra
           agregop +="p"
        agregop+=letra  
         
    return agregop   
if __name__=="__main__":
     palabra= input("Ingresa una palabra: ")
     print(jerigonzo(palabra))

         