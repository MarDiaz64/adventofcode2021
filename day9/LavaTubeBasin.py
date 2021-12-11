#fileOI
input = open('input.txt','r')
hmapStr=[]
h=0
while input:
    line = input.readline().strip()
    if(line == ""):
        break
    hmapStr.append(line)
    h+=1
le=len(hmapStr[0])
hmap=[[0]*le]*h
for i in range(0,h):
    hmap[i]=[int(i) for i in hmapStr[i]]

#find all low points and count risk:
bmax=[-1]*3
basins=[]
riskPoints[]
for i in range(0,h):
    for j in range(0,le):
        c=hmap[i][j]
        down,up,left,right=i+1,i-1,j-1,j+1
        if not((down<h and hmap[down][j]<=c)
           or(up>=0 and hmap[up][j]<=c)
           or(right<le and hmap[i][right]<=c)
           or(left>=0 and hmap[i][left]<=c)):
            riskPoints.append((i,j))
            risk+=c+1
#find the basins:
finished=[]
basNum=0;
for i in range(0,len(riskPoints)):
    c=riskPoints[i]
    x,y=c
    q=[]
    q.append(c)
    finishes.append((x,y,basNum))
    while q !=[]:
        if not (x+1>=h and finished:
            q.append(x+1,y)
        if not x-1<0:
            q.append(x+1,y)
        if not y+1>=le:
            q.append(x+1,y+1)
        if not y-1<0:
            q.append(x+1,y)
        
        
    basNum+=1


           if (check_validity(x1+1,y1))
            q.push(x1+1,y1)
       if (check_validity(x1-1,y1))
            q.push(x1-1,y1)
       if (check_validity(x1,y1+1))
            q.push(x1,y1+1)
       if (check_validity(x1,y1-1))
            q.push(x1,y1-1)
               


print("The sum of the largest lava basin is: ",bmax[0]*bmax[1]*bmax[2])
