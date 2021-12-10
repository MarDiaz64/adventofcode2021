input = open('input.txt','r')
x,y,aim=0,0,0
for line in input.readlines():
    temp = line.split()
    num=int(temp[1])
    if(temp[0]=="forward"):
        x+=num
        y+=aim*num
    elif(temp[0]=="up"):
        aim-=num
    elif(temp[0]=="down"):
        aim+=num
    else:
        print("ERROR BAD READ")
print("At horizontal position: ",x," and depth: ",y," the position is: ", x*y)
