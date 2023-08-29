def palindromo(n):

    k = len(n)


    for i in range(1,k):

        if i == 1:

            if n[k-1]==n[-k]:

                return True
            
            else:
                return False
        
        if palindromo(n) == True:

            return True

        else:

            return False

if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
           