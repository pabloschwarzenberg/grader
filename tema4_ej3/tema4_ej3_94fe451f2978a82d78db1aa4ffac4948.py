def jerigonzo(texto):
    string = ''
    for i in texto:
        jer = ''
        if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
            jer = 'p'+i
        string = string+i+jer
    return string
    
if __name__ == "__main__":
    pass
         