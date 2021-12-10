input = open('input.txt','r')
fish = [int(i) for i in input.read().split(",")]   
for i in range (0,80):
    for j in range(0,len(fish)):
        if(fish[j]!=0):
            fish[j]-=1
        else:
            fish[j]=6
            fish.append(8)
print("The Number of LanternFish after 80 days is: ",len(fish))
        
