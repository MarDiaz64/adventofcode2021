input = open('input.txt','r')
drawnNum = input.readline().split(",")
boards=[][5][5]
bingo=[5][5]
for line in input.readlines()
    if(line !=""):
        for i in range(0,5):
            for j in range(0,5):
                
            


for i in range (0,len(numbers)-2):
    current=int(numbers[i])+int(numbers[i+1])+int(numbers[i+2])
    if(current>previous):
        increasing +=1
    previous=current
print("The number of increasing scans is: ", increasing)
