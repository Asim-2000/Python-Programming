#Average Case: Time = O(Log(n)) || Space = O(Log(n))
# Worst Case: Time = O(N) || Space = O(N)
"""Recursive implementation"""

def FindClosestValueinBST(tree,target):
    return FindingHelper(tree,target,float("inf"))

def FindingHelper(tree,target,closest):
    if tree is None:
        return closest
    if abs(target-closest) > abs(target-tree.value):
        closest=tree.value
    if (target < tree.value):
        return (FindingHelper(tree.left,target,closest))
    elif (target > tree.value):
        return (FindingHelper(tree.right,target,closest))
    else:
        return closest 

#Average Case: Time = O(Log(n)) || Space = O(1)
# Worst Case: Time = O(N) || Space = O(1)
"""Iterative Implementation"""

def FCVBSTIterative(tree, target):
    return HelperFunction(tree,target,float("inf"))

def HelperFunction(tree,target,closest):
    currentNode=tree
    while currentNode is not None:
        if abs(target-closest) > abs (target-currentNode.value):
            closest=currentNode.value
        if (target < currentNode.value):
            currentNode=currentNode.left
        elif (target > currentNode.value):
            currentNode=currentNode.right
        else:
            break

        return closest
