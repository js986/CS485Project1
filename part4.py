import part3
class Node:
    def __init__ (self,data,parent):
        self.data = data
        self.parent = parent
        self.leftChild = None
        self.rightChild = None
        self.height = 0
        #May need to add member for tracking current height of Node

class AVLTree:
    def __init__(self,root):
        self.root = root
        self.traversalCounter = 0

    def insertIter(self,data):
        #print("Inserted Value",data)
        if self.root == None:
            self.root = Node(data,None)
            return
        current = self.root
        while current != None:
            if current.data > data:
                if current.leftChild == None:
                    current.leftChild = Node(data,current)
                    current = current.leftChild
                    break
                current = current.leftChild
                self.traversalCounter+=1
            else:
                if current.rightChild == None:
                    current.rightChild = Node(data,current)
                    current = current.rightChild
                    break
                current = current.rightChild
                self.traversalCounter+=1
        if current == None:
            #print("Node could not be inserted")
            return

        while current != None: #Current should start as the newly inserted node
            #print(current.data)
            current.height = 1 + max(self.findHeight(current.leftChild),self.findHeight(current.rightChild))
            #print("Data is ",current.data,"Height is ", current.height)
            if self.findBalanceFactor(current) > 1:
                #print("Left Imbalanced node ",current.data)
                #There is a left imbalance
                if self.findBalanceFactor(current.leftChild) < 0:
                    #There is a left-right imbalance
                    #print("Left-Right")
                    current.leftChild = self.leftRotation(current.leftChild)
                    current = self.rightRotation(current)
                else:
                    #There is a left-left imbalance
                    current = self.rightRotation(current)
                    #print("Left-Left")
                    #print("Value of ", current.data, current.leftChild.data, current.rightChild.data)
            elif self.findBalanceFactor(current) < -1:
                #print("Right Imbalanced node", current.data)
                #There is a right imbalance
                if self.findBalanceFactor(current.rightChild) <= 0:
                    #There is a right-right imbalance
                    #print("Right-Right")
                    current = self.leftRotation(current)
                else:
                    #There is a right-left imbalance
                    #print("Right-Left")
                    current.rightChild = self.rightRotation(current.rightChild)
                    current = self.leftRotation(current)
            current = current.parent
            self.traversalCounter+=1
        #self.printTree(self.root)
        return self.root

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

        while parent != None:
            parent.height = 1 + max(self.findHeight(parent.leftChild),self.findHeight(parent.rightChild))
            if self.findBalanceFactor(parent) > 1:
                #There is a left imbalance
                if self.findBalanceFactor(parent.leftChild) < 0:
                    #There is a left-right imbalance
                    parent.leftChild = self.leftRotation(parent.leftChild)
                    parent.parent.rightChild = self.rightRotation(parent)
                else:
                    #There is a left-left imbalance
                    parent.parent.leftChild = self.rightRotation(parent)
            elif self.findBalanceFactor(parent) < -1:
                #There is a right imbalance
                if self.findBalanceFactor(parent.rightChild) <= 0:
                    #There is a right-right imbalance
                    parent.parent.rightChild = self.leftRotation(parent)
                else:
                    #There is a right-left imbalance
                    parent.rightChild = self.rightRotation(parent.rightChild)
                    parent = self.leftRotation(parent)

            parent = parent.parent

    def findNextIter(self,node):
        if node.rightChild != None:
            return self.findMinInSubTree(node.rightChild)
        current = node
        while current.parent != None:
            if current.parent > node.data:
                return current.parent
            current = current.parent
            self.traversalCounter+=1
        return None
    def findPrevIter(self,node):
        if node.leftChild != None:
            return self.findMaxInSubTree(node.leftChild)
        current = node
        while current.parent != None:
            if current.parent < node.data:
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

    def printTree(self,node):
        if node == None:
            return
        self.printTree(node.leftChild)
        print(node.data)
        self.printTree(node.rightChild)

    def findHeight(self,node):
        if node == None:
            return -1
        else:
            return node.height

    def findNode(self,index):
        current = self.root
        while current != None:
            if current.data > index:
                current = current.leftChild
            elif current.data < index:
                current = current.rightChild
            else:
                break
        return current

    def findBalanceFactor(self,node):
        return self.findHeight(node.leftChild)-self.findHeight(node.rightChild)

    def rightRotation(self,node):
        if node == None:
            return
        n = node.leftChild
        m = n.rightChild
        n.rightChild = node
        node.leftChild = m
        node.height = 1 + max(self.findHeight(node.leftChild),self.findHeight(node.rightChild))
        n.height = 1 + max(self.findHeight(n.leftChild),self.findHeight(n.rightChild))
        if node.parent != None:
            if node.parent.data > n.data:
                node.parent.leftChild = n
                n.parent = node.parent
                node.parent = n
            else:
                node.parent.rightChild = n
                n.parent = node.parent
                node.parent = n
        else:
            n.parent = None
            node.parent = n
            self.root = n
        #print("result of right rotation ", n.data, n.leftChild.data, n.rightChild.data)
        return n

    def leftRotation(self,node):
        if node == None:
            return
        temp = node
        n = node.rightChild
        m = n.leftChild
        n.leftChild = node
        node.rightChild = m
        node.height = 1 + max(self.findHeight(node.leftChild),self.findHeight(node.rightChild))
        n.height = 1 + max(self.findHeight(n.leftChild),self.findHeight(n.rightChild))
        if temp.parent != None:
            if temp.parent.data > n.data:
                temp.parent.leftChild = n
                n.parent = temp.parent
                node.parent = n
            else:
                temp.parent.rightChild = n
                n.parent = temp.parent
                node.parent = n
        else:
            n.parent = None
            node.parent = n
            self.root = n
        #print("result of left rotation", n.data, n.leftChild.data,n.rightChild.data)
        return n



#Test Cases
"""
root = Node(30,None)
tree = AVLTree(root)
tree.insertIter(15)
tree.insertIter(60)
tree.insertIter(7)
tree.insertIter(22)
tree.insertIter(45)
tree.insertIter(75)
tree.insertIter(17)
tree.insertIter(27)
tree.printTree(root)
print("\n")
print(tree.root.height)
print(tree.findNode(15).height)
print()
print(tree.findMaxIter().data)
print(tree.findMinIter().data)
print("\n")
tree.deleteIter(60)
#print(tree.findNode(30).height)
print("\n")
tree.printTree(root)
"""
#Left-Left Case
"""
lst = part3.getSortedArray(10000)
root = Node(lst[0],None)
tree = AVLTree(root)
for i in range(1,len(lst)):
    tree.insertIter(lst[i])
"""
#Left-Right Case
"""
root = Node(35,None)
tree = AVLTree(root)
tree.insertIter(45)
tree.insertIter(25)
tree.insertIter(30)
tree.insertIter(20)
tree.insertIter(23)
tree.insertIter(15)
"""

#Right-Right Case
"""
root = Node(0,None)
tree = AVLTree(root)
for i in range(1,10000):
    tree.insertIter(i)
"""
#Right-Left Case
"""
root = Node(50,None)
tree = AVLTree(root)
tree.insertIter(25)
tree.insertIter(75)
tree.insertIter(60)
tree.insertIter(80)
tree.insertIter(95)
tree.insertIter(78)
tree.printTree(tree.root)
"""
lst = part3.getRandomArray(10000)
#lst = part3.getSortedArray(10000)
#print(lst)
root = Node(lst[0],None)
tree = AVLTree(root)
for i in range(1,len(lst)):
    tree.insertIter(lst[i])

print(tree.traversalCounter)
#tree.printTree(tree.root)
#print(tree.root.leftChild)
