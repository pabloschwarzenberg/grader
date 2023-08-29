def jerigonzo(string):
    string_nuevo=""
    for i in range(0,len(string)):

        if string[i]=="a" or string[i]=="e" or string[i]=="i" or string[i]=="o" or string[i]=="u":

            string_nuevo+=string[i-1]+string[i]+"p"+string[i]

        i=i+1
    return string_nuevo

if __name__ == "__main__":
    string=input("string: ")
    print (jerigonzo(string))
    
         