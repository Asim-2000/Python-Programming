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

    return closest 
    