def buscarTodas(a,b):

    i=0

    igual=0

    n1=0

    n2=0

    n3=0

    n4=0

    n=0

    for i in range(len(a)):

        if a[i]==b:

           

            if n1 == 0:

                n1=i

                #return n1

            else:

                if n1!=0 and n2==0:

                    n2=i

                    #return n2

                else:

                    if n1!=0 and n2!=0 and n3==0:

                        n3=i

                        #return n3

                    else:

                        if n1!=0 and n2!=0 and n3!=0 and n4==0:

                            n4=i

                            #return n4

                       

            igual+=1

            print(i," ")

       

        else:

            i+=1

    return n1, n2, n3, n4



if __name__ == "__main__":
  a=input("palabra: ")
  b=input("letra: ")
  r=buscarTodas(a,b)
  print(r)
