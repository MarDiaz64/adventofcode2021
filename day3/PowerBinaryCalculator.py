#generate inputs 
input = open('input.txt','r')
numbers = input.read().splitlines()
cNum= numbers.copy()

#values used in script
lenLine=len(numbers[0])
sigBit,oneLeft="0",false

#calculate oxygen
#for every bit position(0->11 in this case)
for bitPos in range(0,lenLine):
    #count the number of 0s and 1s 
    zeros,ones=0,0
    for i in range(0,len(numbers)):
        if((numbers[i])[bitPos]=="0"):
            zeros+=1
        else:
            ones+=1
    #if ones>=zeros:
    if(ones>=zeros):
        sigBit="1"
    else:
        sigBit="0"
    #remove any items in the list that don't meet oxygen specifications
    i=0
    while(i<len(numbers)):
        if(len(oxNum)==1):
            oneLeft=true
            break
        if((numbers[i])[bitPos]!=sigBit):
            numbers.pop(i)
        else:
            i+=1
    if(oneLeft): #stop if only one result left
        break
#calculate c02
#for every bit position(0->11 in this case)
oneLeft=false
for bitPos in range(0,lenLine):
    #count the number of 0s and 1s 
    zeros,ones=0,0
    for i in range(0,len(cNum)):
        if((cNum[i])[bitPos]=="0"):
            zeros+=1
        else:
            ones+=1
    #if ones>=zeros:(inverse of oxygen)
    if(ones>=zeros):
        sigBit="0"
    else:
        sigBit="1"
    #remove any items in the list that don't meet oxygen specifications
    i=0
    while(i<len(cNum)):
        if(len(cNum)==1):
            oneLeft=true
            break
        if((cNum[i])[bitPos]!=sigBit):
            cNum.pop(i)
        else:
            i+=1
    if(oneLeft): #stop if only one result left
        break
#generate and print results
oxygen=int(numbers[0],2)
co2=int(cNum[0],2)
print("Oxygen is: ",oxygen," Co2 is: ",co2, " power is: ",oxygen*co2)
