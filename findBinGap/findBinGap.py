def findBinGap(N):
    currGap=0
    maxGap=0
    isGap = False
    binofN=bin(N)
#    reverse. start from right
    strBin=(binofN[:1:-1])
    print(strBin)
    for i in strBin:
        print (i)
        if (int(i)==1):
#            print("i=1")
            if(not isGap):
                print("i=1 and !isGap")
                currGap = 0
            else :
                if (maxGap<currGap):
                    maxGap = currGap
                    currGap = 0
                    print("i=1 and update maxGap")
#           invert flag        
            isGap = not isGap
            
                    
        else:
            if (isGap):
                print("i=0 and isGap")
                currGap += 1
        print(currGap, maxGap, isGap)
            
    return maxGap


print(findBinGap(1376796946))
