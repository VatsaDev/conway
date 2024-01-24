import random

matmap = []

# 100 rows
for i in range(100):
    matmap.append([])

# 10000 instances, 100x100
for row in matmap:
    for i in range(100):
        row.append(random.randint(0, 1))

def check(x,y):
    n_direct = [[x+1,y],[x-1,y],[x,y+1],[x,y-1]] # connected neighbors
    n_diag = [[x+1,y+1],[x-1,y-1],[x-1,y+1],[x+1,y-1]] # diagnol neighbors

    live_n = 0

    for n in n_direct:
        if (x>=0 and x<=999) and (y>=0 and y<=999): # bounds
            if matmap[x][y]==1:
                live_n += 1
    for n in n_diag:
        if (x>=0 and x<=999) and (y>=0 and y<=999): # bounds
            if matmap[x][y]==1:
                live_n += 1

    return live_n

# loop through all the cells

def update():
    for i in range(len(matmap)):
        for j in matmap[i]:
            if matmap[i][j]==0:
                if check(i,j)==3:
                    matmap[i][j]=1
            if matmap[i][j]==1:
                if check(i,j)==3 or check(i,j)==2:
                    matmap[i][j]=1
                else:
                    matmap[i][j]=0
c = 0
while True:
    update()
    print(matmap)
    c+=1
    if c >4:
        break