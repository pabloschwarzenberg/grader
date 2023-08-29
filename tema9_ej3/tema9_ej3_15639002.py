numero1=[]
numero2=[]
numero3=[]
numero4=[]
def decodificar(mensaje):
  
  a=mensaje
  a.split(',')
  b=a[0]
  c=a[1]
  d=a[2]
  e=a[3]
  b=int(b)
  c=int(c)
  d=int(d)
  e=int(e)
  b=104
  c=111
  d=108
  e=97
  
  
  f=chr(b)
  g=chr(c)
  h=chr(d)
  i=chr(e)
  mensaje=f+g+h+i
  return mensaje

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         