class Node:
    def __init__(self,data,parent):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.parent = parent

class RecBST:
    def __init__(self,root):
        self.root = root

    def insertRec(self,root,data):
        if root == None:
            root = Node(data,None)
            return root
        elif root.data > data:
            root.leftChild = self.insertRec(root.leftChild,data)
            root.leftChild.parent = root
        else:
            root.rightChild = self.insertRec(root.rightChild,data)
            root.rightChild.parent = root
        return root

    def deleteRec(self,root,index):
        if root == None:
            return root
        if root.data > index:
            root.leftChild = self.deleteRec(root.leftChild,index)
        elif root.data < index:
            root.rightChild = self.deleteRec(root.rightChild,index)
        else:
            if root.leftChild == None and root.rightChild == None:
                root = None
                return root
            elif root.leftChild == None:
                root.rightChild.parent = root.parent
                root = root.rightChild
                return root
            elif root.rightChild == None:
                root.leftChild.parent = root.parent
                root = root.leftChild
                return root
            else:
                min = self.findMin(root.rightChild)
                min.parent = root.parent
                root = min
                root.rightChild = deleteRec(root.rightChild,min.data)
        return root


    def findNextRec(self,node):
        if node.rightChild != None:
            return self.findMinRec(node.rightChild)
        if node.parent != None:
            if node.parent.data > node.data:
                return node.parent
            else:
                self.findNextRec(node.parent)
        return None

    def findPrevRec(self,node):
        if node.leftChild != None:
            return self.findMaxRec(node.rightChild)
        if node.parent != None:
            if node.parent.data < node.data:
                return node.parent
            else:
                self.findPrevRec(node.parent)
        return None

    def findMinRec(self,node):
        if node.leftChild == None:
            return node
        else:
            self.findMinRec(node.leftChild)

    def findMaxRec(self,node):
        if node.rightChild == None:
            return node
        else:
            self.findMaxRec(node.rightChild)

    def printTree(self,node):
        if node == None:
            return
        self.printTree(node.leftChild)
        print(node.data)
        self.printTree(node.rightChild)
