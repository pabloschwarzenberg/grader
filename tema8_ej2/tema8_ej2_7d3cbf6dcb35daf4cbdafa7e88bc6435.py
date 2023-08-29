def buscarTodas(a,b):
    a_l=list(a)
    respuesta=[]
    i=0
    while i < len(a_l):
        m=a_l[i]
        if m in b:
          respuesta.append(str(a_l.index(b)))
          respuesta.append(' ')
          p=a_l.index(b)
          a_l[p]="*"
          continue
        i=i+1
    helado=''.join(respuesta)
    return(helado.strip(" "))

v=buscarTodas("tres tristes tigres","t")

           