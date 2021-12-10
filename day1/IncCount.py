input = open('input.txt','r')
previous, current, increasing=10000,0,0
for line in input.readlines():
    current = int(line);
    if(current>previous):
        increasing =increasing+1
    previous=current;
print("The number of increasing scans is: ", increasing)
