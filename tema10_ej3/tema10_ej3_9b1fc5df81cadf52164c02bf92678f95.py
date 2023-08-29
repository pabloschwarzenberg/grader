def sopaletras(T,L):
    archivo = open(T,'r')
    SOPA = archivo.readlines()
    archivo.close()
    
    sopa = []
    for linea in SOPA:
        print(linea)
        linea = linea.lower()
        sopa.append(linea)
    s = ''.join(sopa)
    print(s)
    s = list(s)

    for asd in s:
        if asd==' ':
            del s[s.index(asd)]

    s = ''.join(s)
    print(s)

    sopa = s.split('\n')

    der = False
    abajo = False
    diagonal = False
    for palabra in L:
        #print(palabra)
        for linea in sopa:
            c = sopa.index(linea)
            #print('n° linea=',c)
            a = linea.find(palabra)
            #print(a)
            if a!=-1:
                print('({0},[{1},{2}],{3})'.format(palabra,c,a,'derecha'))
                der = True
                break
            if a==-1 and c<len(sopa)-1:
                continue
            else:
                b = linea.find(palabra[0])
                #print(b)
                d = 1
                e = 1
                if b!=-1:
                    if sopa[c+1][b]==palabra[1]:#abajo                    
                        for LINEA in range(c+2,len(palabra)):
                            if LINEA<len(sopa):
                                if sopa[LINEA][b]==palabra[d]:
                                    d += 1
                                else:
                                    break
                            else:
                                break
                            
                            if d==len(palabra):
                                print('{0},[{1},{2}],{3}'.format(palabra,c,b,'abajo'))
                                abajo = True
                                break

                    if sopa[c+1][b+1]==palabra[1] and abajo==False:#diagonal
                        f = b+2
                        for l in range(c+2,len(palabra)):
                            if l<len(sopa):
                                if sopa[l][f]==palabra[d]:
                                    d += 1
                                    f += 1
                            else:
                                break
                            if d==len(palabra):
                                print('{0},[{1},{2}],{3}'.format(palabra,c,b,'diagional'))
                                diagonal = True
                                break

        if der==True or abajo==True or diagonal==True:
            continue


    return [(palabras[0],[0,0],"diagonal")]

if __name__=="__main__":
    print(sopaletras("sopa.txt",["cra"]))
    print(sopaletras("sopa.txt", ["aro"]))
    print(sopaletras("sopa.txt", ["casa"]))
    print(sopaletras("sopa.txt",["casa","cra","aro"]))

           