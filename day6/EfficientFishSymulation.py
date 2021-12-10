input = open('input.txt','r')
fish = [int(i) for i in input.read().split(",")]
frequency=[0]*9 
numOfFish=len(fish)
for i in range(0, len(fish)):
    if(fish[i]==0):
        frequency[0]+=1
    elif(fish[i]==1):
        frequency[1]+=1
    elif(fish[i]==2):
        frequency[2]+=1
    elif(fish[i]==3):
        frequency[3]+=1
    elif(fish[i]==4):
        frequency[4]+=1
    elif(fish[i]==5):
        frequency[5]+=1
    elif(fish[i]==6):
        frequency[6]+=1
    elif(fish[i]==7):
        frequency[7]+=1
    else:
        frequency[8]+=1
for i in range (0,256):
    t0 =frequency[0]
    numOfFish+=t0
    frequency[0]=frequency[1]
    frequency[1]=frequency[2]
    frequency[2]=frequency[3]
    frequency[3]=frequency[4]
    frequency[4]=frequency[5]
    frequency[5]=frequency[6]
    frequency[6]=frequency[7]+t0
    frequency[7]=frequency[8]
    frequency[8]=t0
print("The Number of LanternFish after 256 days is: ",len(fish))
