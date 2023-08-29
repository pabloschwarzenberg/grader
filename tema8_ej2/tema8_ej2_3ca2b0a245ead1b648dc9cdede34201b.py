def buscarTodas(a,b):
    string= ""
    for i in range(len(a)):
        if a[i] == b:
            string= string + str(i) + " "
    return string[:len(string)-1]

if __name__ == "__main__":
    string1= "tres tristes tigres"
    string2= "t"
    print(buscarTodas(string1,string2))
    pass