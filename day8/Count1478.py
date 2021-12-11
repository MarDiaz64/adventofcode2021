input = open('input.txt','r')
data=[]
counter=0
for line in input.read().splitlines():
    output=line.split("|")
    for element in output[1].split():
        data.append(element)
for output in data:
    if(len(output)!=5 and len(output)!=6):
        counter+=1
print("Number of 1,4,7,and 8s are:",counter)

