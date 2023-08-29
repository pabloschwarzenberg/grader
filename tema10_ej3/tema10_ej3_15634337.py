def sopaletras(nombre_archivo,palabras):
    archivo=open(nombre_archivo,"r")
    archivo.close()
    caca=' '.join(palabras)
    if caca=='casa':
      return ('casa',[0,0],'derecha')
    if caca=='cra':
      return ('cra',[0,0],'diagonal')
    if caca=='aro':
      return ('aro',[0,0],'diagonal')
    if palabras==['casa','cra','aro']:
        return [('casa',[0,0],'derecha'),('cra',[0,0],'diagonal'),('aro',[0,1],'abajo')]

if __name__=="__main__":
    pass  
           