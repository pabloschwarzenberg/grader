def sopaletras(nombre_archivo,palabras):
    archivo=open(nombre_archivo,"r")
    file=archivo.readlines()
    matriz=[]
    for tmp in file:
        matriz.append((tmp.replace("\n","")).replace(" ",""))
    resupala=[]
    posiciones=[]
    forma=[]
    
    for ll in palabras:
        pal=ll
        for i in range(0,len(matriz)):
            acu=""
            for j in range(0,len(matriz[i])):
                acu=acu+matriz[i][j]
                if(acu==pal):
                    resupala.append(pal)
                    posiciones.append([i,j-(len(pal)-1)])
                    forma.append("derecha")
                    
                for ini in range(1,j):
                    if(str(matriz[i][ini:(j+1)])==pal):
                        resupala.append(pal)
                        posiciones.append([i,ini])
                        forma.append("derecha")

        #vertical
        for i in range(0,len(matriz[i])):
            acu2=""
            for j in range(0,(len(matriz))):
                acu2=acu2+matriz[j][i]
                if(acu==pal):
                    resupala.append(pal)
                    posiciones.append([j-(len(pal)-1),i])
                acu3=""
                ll=0
                vpp=0
                vii=0
                for pp in range(1,j):
                    acu3=acu3+matriz[pp][i]
                    if(ll==0):
                        vpp=i
                        vii=pp
                    else:
                        ll=1
                if(acu3==pal):
                    resupala.append(pal)
                    posiciones.append([vii,vpp])
                    forma.append("abajo")
                acu4=""
                gg=0
                ttt=0
                jjj=0
                for qq in range(j,len(matriz)):
                    acu4=acu4+matriz[qq][i]
                    if(gg==0):
                        ttt=i
                        jjj=qq
                    else:
                        gg=1
                if(acu4==pal):
                    resupala.append(pal)
                    posiciones.append([jjj+1-len(acu4),ttt])
                    forma.append("abajo")

            
        #diagonal

        matt=[]
        matrizGuarda=matriz
        for ll in matriz:
            su=""
            cf=list(ll)
            cf.reverse()
            for oo in cf:
                su=su+(oo)
            matt.append(su)
        #print(matt)
        
        #matriz=matrizGuarda
        matriz=matt
        

        n=len(matriz[1])
        m=len(matriz)
        cantDiagonales=n+m-1
        num=0
        for diagonal in range(0,cantDiagonales):
            l=0
            if (diagonal>m-1):
                l=m-1
            else:
                l=diagonal
            x=l
            y=l
            acu=""
            posx=0
            posy=0
            rr=0
            while(y>=0 and (diagonal-y)<n):
                x=diagonal-y
                acu=acu+matriz[y][x]
                #if(rr==0):
                posx=x
                posy=y
                rr=1
                y=y-1
            rr=1
            volt=""
            we=list(acu)
            we.reverse()
            
                
            for ko in we:
                volt=volt+ko
            acu=volt
            for i in range(len(acu)):
                acu4=""
                for j in range(i,len(acu)):
                    acu4=acu4+acu[j]
                if (acu4==pal):
                    resupala.append(pal)
                    posiciones.append([posy,abs(posx-len(matriz))])
                    forma.append("diagonal")
            acu5=""
            for k in range(0,j):
                acu5=acu5+acu[k]
            if (acu5==pal):
                resupala.append(pal)
                posiciones.append([posy,abs(posx-len(matriz))])
                forma.append("diagonal")

        archivo.close()
    return[(resupala,posiciones,forma)]
    
if __name__ == "__main__":
    
    print(sopaletras("sopa.txt",["cra"]))
    print(sopaletras("sopa.txt",["aro"]))
    print(sopaletras("sopa.txt",["casa"]))
    print(sopaletras("sopa.txt",["casa","cra","aro"]))
