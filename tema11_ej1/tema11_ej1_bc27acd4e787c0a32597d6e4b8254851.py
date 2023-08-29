def palindromo(string):
    string=string.strip()
    if len(string)==1:
         return True
    elif len(string)==2 and string[0]==string[1]:
        return True
    else:
        if string[0]==string[len(string)-1]:
            lista=list(string)
            lista.pop(0)
            lista.pop(len(lista)-1)
            string=""
            for elemento in lista:
                string=string+str(elemento)
            return palindromo(string)
        else:
            return False


if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
           