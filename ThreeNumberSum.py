def ThreeNumSum(array,targetSum):
    array.sort()
    triplets=[]
    #Since we want triplet, we want the fixed number to go as far as the 3rd last value in array
    #so that we can have left and right pointer too.
    for i in range(len(array)-2):
        