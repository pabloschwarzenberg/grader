def amigos(a,b):
    ads = 0
    bds = 0
    for ad in range(1, a):
          if a % ad == 0:
              ads += ad
              print(ads)
    for bd in range(1, b):
          if b % bd == 0:
              bds += bd
              print(bds)
    if (bds == a) and (ads == b):
          return True
    else:
          return False
           