import math
input = open('input.txt','r')
crabs = [int(i) for i in input.read().split(",")]
#calulate mean(point)
mean=0
for i in range(0,len(crabs)):
    mean+=crabs[i]
point=math.floor(mean/len(crabs))
print("The most efficient point: ",point)

#calculate the fuel to get to the mean:
fuel =0
for i in range(0,len(crabs)):
    fact=0
    for j in range(1,abs(crabs[i]-point)+1):
        fact = fact + j
    fuel+=fact
print("The fuel to get to that point is: ",fuel)
