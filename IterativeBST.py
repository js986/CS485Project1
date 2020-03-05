class Node:
    def __init__(self,data,parent):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.parent = parent

class IterBST:
    def __init__(self,root):
        self.root = root
        self.traversalCounter = 0

    def insertIter(self,data):
        if self.root == None:
            self.root = Node(data,parent)
            return
        current = self.root
        while current != None:
            if current.data > data:
                if current.leftChild == None:
                    current.leftChild = Node(data,current)
                    break
                current = current.leftChild
                self.traversalCounter+=1
            else:
                if current.rightChild == None:
                    current.rightChild = Node(data,current)
                    break
                current = current.rightChild
                self.traversalCounter+=1
        return

    def deleteIter(self,data):
        current = self.root
        while current != None:
            if current.data > data:
                current = current.leftChild
                self.traversalCounter+=1
            elif current.data < data:
                current = current.rightChild
                self.traversalCounter+=1
            else:
                break
        if current == None:
            #print("The node could not be found")
            return
        if current.leftChild == None and current.rightChild == None:
            if current.parent != None:
                parent = current.parent
                if current.parent.leftChild == current:
                    current.parent.leftChild = None
                else:
                    current.parent.rightChild = None
            current = None
        elif current.leftChild == None:
            current.rightChild.parent = current.parent
            current = current.rightChild
            parent = current.parent
        elif current.rightChild == None:
            current.leftChild.parent = current.parent
            current = current.leftChild
            parent = current.parent
        else:
            temp = self.findNextIter(current)
            current.data = temp.data
            if temp.parent != None:
                if temp.parent.leftChild == temp:
                    temp.parent.leftChild = None
                else:
                    temp.parent.rightChild = None
                temp.parent = current.parent
                parent = temp.parent
                temp = None

    def findNextIter(self,node):
        if node.rightChild != None:
            return self.findMinInSubTree(node.rightChild)
        current = node
        while current.parent != None:
            if current.parent.data > node.data:
                return current.parent
            current = current.parent
            self.traversalCounter+=1
        return None

    def findPrevIter(self,node):
        if node.leftChild != None:
            return self.findMaxInSubTree(node.leftChild)
        current = node
        while current.parent != None:
            if current.parent.data < node.data:
                return current.parent
            current = current.parent
            self.traversalCounter+=1
        return None

    def findMinIter(self):
        current = self.root
        while current.leftChild != None:
            current = current.leftChild
            self.traversalCounter+=1
        return current

    def findMaxIter(self):
        current = self.root
        while current.rightChild != None:
            current = current.rightChild
            self.traversalCounter+=1
        return current

    #Helper Functions
    def findMaxInSubTree(self,node):
        current = node
        while current.rightChild != None:
            current = current.rightChild
            self.traversalCounter+=1
        return current

    def findMinInSubTree(self,node):
        current = node
        while current.leftChild != None:
            current = current.leftChild
            self.traversalCounter+=1
        return current
