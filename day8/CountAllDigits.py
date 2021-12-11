input = open('input.txt','r')
counter=0
for line in input.read().splitlines():
    output,sigPat=[],[]
    data=line.split("|")
    #get outputs:
    for element in data[1].split():
        output.append(element)

    #get signal patterns:
    for element in data[0].split():
        sigPat.append(element)
        
    #lazy insersion sort implementation
    for i in range(1,len(sigPat)):
        j=i
        while j>0 and len(sigPat[j-1])>len(sigPat[j]):
            temp = sigPat[j]
            sigPat[j]=sigPat[j-1]
            sigPat[j-1]=temp
            j=j-1
        i+=1
    
    
    #find specified groups using 1,4,7,8
    a,cf,bd,eg=[],[],[],[]
    for sig in sigPat:
        if(len(sig)==2): #1
            if not(sig[0] in cf or sig[1] in cf):
                cf.append(sig[0])
                cf.append(sig[1])
        elif(len(sig)==3): #7
            for c in sig:
                if not(c in a or c in cf):
                    a.append(c)
                    break
        elif(len(sig)==4):#4
            for c in sig:
                if not(c in bd or c in a or c in cf):
                    bd.append(c)
        elif(len(sig)==7):#8
            for c in sig:
                if not((c in eg) or c in a or c in cf or c in bd):
                    eg.append(c)
    #find output
    temp=""
    for el in output:
        if(len(el)==2): #1
            temp+="1"
        elif(len(el)==3): #7
            temp+="7"
        elif(len(el)==4):#4
            temp+="4"
        elif(len(el)==7):#8
            temp+="8"
        elif(len(el)==5):#2,3,5
            if(cf[0] in el and cf[1] in el):
                temp+="3"
            elif(bd[0] in el and bd[1] in el):
                temp+="5"
            else:
                temp+="2"
        else: #len=6 | 0,6,9
            if(bd[0] in el and bd[1] in el):
                if(cf[0] in el and cf[1] in el):
                    temp+="9"
                else:
                    temp+="6"
            else:
                temp+="0"
    counter+=int(temp)
print("Sums of output lines:",counter)

