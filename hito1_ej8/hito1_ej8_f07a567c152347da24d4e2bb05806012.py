n = int(input())

un = n%10
de = (n//10)%10
ce = (n//100)%10
mi = (n//1000)%10

print("{}M + {}C + {}D + {}U".format(mi,ce,de,un))

      

      