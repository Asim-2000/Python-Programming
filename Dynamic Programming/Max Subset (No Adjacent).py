def maxSubsetSumNoAdjacent(array):
    if not len(array):
        return
    elif (len(array))==1:
        return array[0]
    maxSums=array[:]
    maxSums[1]=max