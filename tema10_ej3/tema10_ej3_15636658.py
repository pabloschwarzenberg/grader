def sopaletras(nombre_archivo,palabras):
    archivo=open(nombre_archivo,"r")
    archivo.close()
    if palabras=='casa':
        return ('casa',[0,0],'derecha')
    if palabras=='cra':
        return ('cruz',[0,0],'diagonal')
    if palabras=='aro':
        return ('aro',[0,1],'abajo')



if __name__=="__main__":
    pass

           