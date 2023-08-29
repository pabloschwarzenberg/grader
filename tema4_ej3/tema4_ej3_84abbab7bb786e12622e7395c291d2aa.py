#Crea una función, que reciba un texto, y retorne el mismo texto traducido a jerigonzo. El Jerigonzo, es un idioma en que después de cada vocal, se agrega una p, y repite la vocal.
def jerigonzo(string):
    n=len(string)
    string=list(string)
    for i in range(0,n):
        if string[i]=='a':
            string[i]='apa'
        elif string[i]=='e':
            string[i]='epe'
        elif string[i]=='i':
            string[i]='ipi'
        elif string[i]=='o':
            string[i]='opo'
        elif string[i]=='u':
            string[i]='upu'
    string=''.join(string)
        
    return string

if __name__ == "__main__":
    string=input('Ingrese palabra: ')
    print(jerigonzo(string))
    
    pass
