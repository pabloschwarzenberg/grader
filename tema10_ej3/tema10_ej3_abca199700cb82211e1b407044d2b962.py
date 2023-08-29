def sopaletras(nombre_archivo,palabras):
  archivo=open(nombre_archivo,"r")
  archivo.close()
  file = open("sopaletras.txt","r")
  pa = 1
  for linea in file.readlines():
    print("Revisando",pa)
    if nombre_archivo in lines.lower():
      return pa
    pa +=1
    
  return -1
  print("No se encontró")
  
  palabras("cra aro casa qwertyuiopasdfghjklñzxcvbnm".lower())
   

           