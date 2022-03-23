howmuchtohave = {}

for i in range(4):
    howmuchtohave[(4,i)] = 100

for i in range(4):
    howmuchtohave[(i,4)] = -100

for i in range(3,-1,-1):
    for j in range(3,-1,-1):
        #print(type((i,j)))
        howmuchtohave[(i,j)] = (1/2)*(howmuchtohave[(i+1,j)] + howmuchtohave[(i,j+1)])

def howmuchto_bet(a,b):
    return howmuchtohave[(a+1,b)]-howmuchtohave[(a,b)]

print(howmuchto_bet(0,0))
