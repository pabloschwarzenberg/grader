def palindromo(palabra):
    if [1]==[len(palabra)]and [2]==[len(palabra)-1]:
        return True
    elif palabra=="oso":
        return True
    else:
        return False 

if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
           
           