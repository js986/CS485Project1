class Node:
    def __init__(self,data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

def insertRec(root,data):
    if root == None:
        root = Node(data)
    elif root.data > data:
        insertRec(root.leftChild,data)
    else:
        insertRec(root.leftChild,data)

def delete(root,index):
    return 0


def findPrevRec(root):
    if root == None:
        return root
    return root.leftChild

def findNextRec(root):
    if root == None:
        return root
    return root.rightChild

def findMinRec(root):
    if root == None:
        return root
    elif root.leftChild == None:
        return root
    else:
        findMinRec(root.leftChild)

def findMaxRec(root):
    if root == None:
        return root
    elif root.rightChild == None:
        return root
    else:
        findMaxRec(root.rightChild)
