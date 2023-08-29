def sopaletras(nombre_archivo,palabras):


    sopita=open(nombre_archivo,"r")
    lines=list(sopita)
    
    for linea in lines:
        if lines.index(linea)!=len(lines)-1:
            pos=lines.index(linea)
            lines.pop(pos)
            linea=list(linea)
            linea.pop(-1)
            linea="".join(linea)
            lines.insert(pos,linea)
    
    sopita.close()
    
    sopita=[]
    for linea in lines:
        lineamat=linea.split(" ")
        sopita.append(lineamat)
    
    sopita_horizontal=[]
    for linea in sopita:
        sopita_horizontal.append("".join(linea))
    
    sopita_vertical=[]
    for numcol in range(len(sopita[0])):
        columna=""
        for numfil in range(len(sopita)):
            columna+=sopita[numfil][numcol]
        sopita_vertical.append(columna)
    
    letras=len(sopita_horizontal)*len(sopita_vertical)
    if letras%2==0:
        tot_diags=letras//2
    elif letras%2==1:
        tot_diags=(letras+1)//2
    
    sopita_diagonal=[]
    finfil=len(sopita_horizontal)-1
    fincol=len(sopita_vertical)-1
    numdiag=0
    startpos=[0,0]
    while numdiag<tot_diags:
        if numdiag>=finfil:
            startpos[1]=0
            startpos[0]=numdiag-finfil
        else:
            startpos[0]=0
            startpos[1]=finfil-numdiag
        diago=""
        numfil=startpos[1]
        numcol=startpos[0]
        while 0<=numfil<=finfil and 0<=numcol<=fincol:
            diago+=sopita[numfil][numcol]
            numfil+=1
            numcol+=1
        sopita_diagonal.append(diago)
        numdiag+=1
    
    resultadosh=[]
    resultadosv=[]
    resultadosd=[]
    for parola in palabras:
        palabra=parola.upper()
        for fila in sopita_horizontal:
            direct="derecha"
            if fila.find(palabra)!=-1:
                poscol=fila.find(palabra)
                posfil=sopita_horizontal.index(fila)
                resultadosh.append((parola,[posfil,poscol],direct))
        for columna in sopita_vertical:
            direct="abajo"
            if columna.find(palabra)!=-1:
                poscol=sopita_vertical.index(columna)
                posfil=columna.find(palabra)
                resultadosv.append((parola,[posfil,poscol],direct))
        for diagonal in sopita_diagonal:
            direct="diagonal"
            if diagonal.find(palabra)!=-1:
                if sopita_diagonal.index(diagonal)<=finfil:
                    posfil=finfil-sopita_diagonal.index(diagonal)+diagonal.find(palabra)
                    poscol=diagonal.find(palabra)
                else:
                    posfil=diagonal.find(palabra)
                    poscol=sopita_diagonal.index(diagonal)-finfil+diagonal.find(palabra)
                resultadosd.append((parola,[posfil,poscol],direct))
    
    allres=[]
    allres.extend(resultadosh)
    allres.extend(resultadosv)
    allres.extend(resultadosd)
    return allres

if __name__=="__main__":
    print(sopaletras("sopa.txt",["cra"]))
    print(sopaletras("sopa.txt", ["aro"]))
    print(sopaletras("sopa.txt", ["casa"]))
    print(sopaletras("sopa.txt",["casa","cra","aro"]))