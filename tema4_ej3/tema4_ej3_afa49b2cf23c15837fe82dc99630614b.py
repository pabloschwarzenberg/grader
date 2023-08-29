def jerigonzo(string):
        texto=string
        
        string=string.replace("a","apa")
        string=string.replace("e","epe")
        string=string.replace("i","ipi")       
        string=string.replace("o","opo")
        string=string.replace("u","upu")




        return string

if __name__ == "__main__":
    string=input("inserte un texto:")
    
    print(jerigonzo(string))
         
