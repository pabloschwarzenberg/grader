      def secuencia(string):
    string=string.upper()
    lista=[]
    ver=True
    for i in range(1,len(string),2):
        par=string[i:i+2]
        if par[0] in 'ACTG' and par[1] in 'ACTG':
            if par[0]=='A':
                if par[1]=='T':
                    ver=False
            elif par[0]=='C':
                if par[1]=='G':
                    ver=False
            elif par[0]=='T':
                if par[1]=='A':
                    ver=False
            else:
                if par[1]=='C':
                    ver=False
    return ver
if __name__=='__main__':
    cadena=input('ingrese secuencia: ')
    if secuencia(cadena):
        print('Secuencia correcta')
    else:
        print("secuencia incorrecta")