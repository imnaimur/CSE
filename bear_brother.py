n,m = map(int,input().split())
i = 1
lim = n
bob = m
while True:
   lim *= 3 
   bob *= 2
   if lim > bob:
        break
   i+= 1
print(i)