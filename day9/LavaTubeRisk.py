#fileOI
input = open('input.txt','r')
risk=0
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
riskPoints=[]
for i in range(0,h):
    for j in range(0,le):
        c=hmap[i][j]
        down=i+1
        up=i-1
        left=j-1
        right=j+1
        if not((down<h and hmap[down][j]<=c)
           or(up>=0 and hmap[up][j]<=c)
           or(right<le and hmap[i][right]<=c)
           or(left>=0 and hmap[i][left]<=c)):
            riskPoints.append(c)
            risk+=c+1
print(riskPoints)
print("The risk of the lava low points is: ",risk)
