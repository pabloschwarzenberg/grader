def rot13(palabra):

    x = list(palabra)

    i=0

    while i<len(x):

        if x[i]=='a':
            x[i]='n'

        elif x[i]=='b':
            x[i]='o'

        elif x[i]=='c':
            x[i]='p'

        elif x[i]=='d':
            x[i]='q'

        elif x[i]=='e':
            x[i]='r'

        elif x[i]=='f':
            x[i]='s'

        elif x[i]=='g':
            x[i]='t'

        elif x[i]=='h':
            x[i]='u'

        elif x[i]=='i':
            x[i]='v'

        elif x[i]=='j':
            x[i]='w'

        elif x[i]=='k':
            x[i]='x'

        elif x[i]=='l':
            x[i]='y'

        elif x[i]=='m':
            x[i]='z'


###
        elif x[i]=='n':
            x[i]='a'

        elif x[i]=='o':
            x[i]='b'

        elif x[i]=='p':
            x[i]='c'

        elif x[i]=='q':
            x[i]='d'

        elif x[i]=='r':
            x[i]='e'

        elif x[i]=='s':
            x[i]='f'

        elif x[i]=='t':
            x[i]='g'

        elif x[i]=='u':
            x[i]='h'

        elif x[i]=='v':
            x[i]='i'

        elif x[i]=='w':
            x[i]='j'

        elif x[i]=='x':
            x[i]='k'

        elif x[i]=='y':
            x[i]='l'

        elif x[i]=='z':
            x[i]='m'

        i=i+1

    traduccion = ''.join(x)

    return traduccion
