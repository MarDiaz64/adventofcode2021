#definition: "geometric median of a discrete set of sample points in a Euclidean space
#is the point minimizing the sum of distances to the sample points."
#FIND THE MEDIAN! :D
input = open('test.txt','r')
crabs = [int(i) for i in input.read().split(",")]
point=0

#lazy insersion sort implementation
for i in range(1,len(crabs)):
    j=i
    while j>0 and crabs[j-1]>crabs[j]:
        temp = crabs[j]
        crabs[j]=crabs[j-1]
        crabs[j-1]=temp
        j=j-1
    i+=1
print(len(crabs)/2)
point=crabs[int(len(crabs)/2)]
print("The most fuel efficient point is: ", point)

#calculate the fuel to get to the median:
fuel =0
for i in range(0,len(crabs)):
    fuel+=abs(crabs[i]-point)
print("The fuel to get to that point is: ",fuel)
