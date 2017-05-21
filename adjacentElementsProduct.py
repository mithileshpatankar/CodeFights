def adjacentElementsProduct(inputArray):
    mylist=list()
    for i in range(len(inputArray)-1):
        mylist.append(inputArray[i]*inputArray[i+1])    
    return max(mylist)
        
        
        


        

