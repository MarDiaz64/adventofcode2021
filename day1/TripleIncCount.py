input = open('input.txt','r')
previous, current, increasing=30000,0,0
numbers = input.read().splitlines()
for i in range (0,len(numbers)-2):
    current=int(numbers[i])+int(numbers[i+1])+int(numbers[i+2])
    if(current>previous):
        increasing +=1
    previous=current
print("The number of increasing scans is: ", increasing)
