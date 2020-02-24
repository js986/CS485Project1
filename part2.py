class Node:
    def __init__(self,value):
        self.value = value
        self.leftChild = None
        self.rightChild = None

def sort(root):
    if root == None:
        return
    sort(root.leftChild)
    print(root.value)
    sort(root.rightChild)
