#Time=O(V+E) || Space = O(V)

class Node:
    def __init__(self,name):
        self.chilren=[]
        self.name=name

    def addChild(self,name):
        self.children.append(Node(name))

    def depthFirstSearch(self,array):
        array.append(self.name)
        for child in self.children:
            self.children.depthFirstSearch(array)
        return array

