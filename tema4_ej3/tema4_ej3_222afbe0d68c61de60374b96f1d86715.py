vocal =['a','e','i','o','u']
def jerigonzo(string):
    string=list(string)
    i=0
    while i < (len(string)):
    
        if string[i] in vocal:
            string[i] = string[i]+ 'p'+string[i]
        i=i+1    
    
       
      
    string=''.join(string)
    return string

if __name__ == "__main__":
 string=input('Ingrese la palabra a traducir:: ')
 print(jerigonzo(string))
