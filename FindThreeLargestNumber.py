#time=O(n) || space= O(1)

def FindThreeLargest(array):
    ThreeLargest=[None,None,None]
    for num in array:
        UpdateThreeLargest(ThreeLargest,num)
    return ThreeLargest


def UpdateThreeLargest(ThreeLargest,num):
    if (ThreeLargest[2] is None or num > ThreeLargest[2]):
        ShiftandUpdate(ThreeLargest,num,2)
    elif (ThreeLargest[1] is None or num > ThreeLargest[1]):
        ShiftandUpdate(ThreeLargest,num,1)
    elif (ThreeLargest[0] is None or num > ThreeLargest[0]):
        ShiftandUpdate(ThreeLargest,num,0)


def ShiftandUpdate(array,num,idx):
    for i in range(idx+1):
        if (i==idx):
            array[i]=num
        else:
            array[i]=array[i+1]
