#Time=O(N^2) || Space= O(N)
def ThreeNumSum(array,targetSum):
    array.sort()
    triplets=[]
    #Since we want triplet, we want the fixed number to go as far as the 3rd last value in array
    #so that we can have left and right pointer too.
    for i in range(len(array)-2):
        left=i+1
        right=len(array)-1
        while left < right:
            CurrentSum= array[i]+array[left]+array[right]
            if CurrentSum==targetSum:
                triplets.append([array[i],array[left],array[right]])
                left+=1
                right-=1
            elif CurrentSum < targetSum:
                left+=1
            elif CurrentSum > targetSum:
                right-=1
        
    return triplets