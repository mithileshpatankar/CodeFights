def makeArrayConsecutive2(statues):
    count=0
    listsorted=sorted(statues)
    for i in range(len(listsorted)-1):
        if listsorted[i]+1!=listsorted[i+1]:
            for j in range(1,100):
                if listsorted[i]+j==listsorted[i+1]:
                    count=count+(j-1)
    return count
