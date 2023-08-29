def rot13(a):
  b=list(a)
  for i in range(len(a)):
    c=b[i]
    if c=='a':
      b[i]='n'
    elif c=='b':
      b[i]='o'
    elif c=='c':
      b[i]='p'
    elif c=='d':
      b[i]='q'
    elif c=='e':
      b[i]='r'
    elif c=='f':
      b[i]='t'
    elif c=='h':
      b[i]='u'
    elif c=='i':
      b[i]='v'
    elif c=='j':
      b[i]='w'
    elif c=='k':
      b[i]='x'
    elif c=='l':
      b[i]='y'
    elif c=='m':
      b[i]='z'
    elif c=='n':
      b[i]='a'
    elif c=='o':
      b[i]='b'
    elif c=='p':
      b[i]='c'
    elif c=='q':
      b[i]='d'
    elif c=='r':
      b[i]='e'
    elif c=='s':
      b[i]='f'
    elif c=='t':
      b[i]='g'
    elif c=='u':
      b[i]='h'
    elif c=='v':
      b[i]='i'
    elif c=='w':
      b[i]='j'
    elif c=='x':
      b[i]='k'
    elif c=='y':
      b[i]='l'
    elif c=='z':
      b[i]='m'  
    m=''.join(b)
    return m
      
    

if __name__=="__main__":
    m=str(input("Ingresa la palabra que quieras encriptar: "))
    print(rot13(m))
           