#Time= O(NlogN+MlogM) where N is the len of array 1 and M is the len of array 2 
#Space =O(1)

def SmallestDifference(array1,array2):
    array1.sort()
    array2.sort()
    idx1=0
    idx2=0
    smallest=float('inf')
    current=float('inf')
    smallestpair=[]
    
    while (idx1 < len(array1) and idx2 < len(array2)):
        firstnum=array1[idx1]
        secondnum=array2[idx2]
        if firstnum < secondnum :
            current= secondnum - firstnum
            idx1+=1
        elif firstnum > secondnum :
            current=firstnum-secondnum
            idx2+=1
        # else condition is firstnum==secondnum which can be the smallest difference     
        else:
             return [firstnum,secondnum]
        if current<smallest:
            smallest=current
            smallestpair=[firstnum,secondnum]
    return smallestpair
