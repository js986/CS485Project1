class Node:
    def __init__(self,data,parent=None):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.parent = parent

def insertRec(root,data,parent=None):
    if root == None:
        root = Node(data,parent)
        return root
    elif root.data > data:
        root.leftChild = insertRec(root.leftChild,data,root)
    else:
        root.rightChild = insertRec(root.rightChild,data,root)
    return root

def deleteRec(root,index):
    if root == None:
        return root
    if root.data > index:
        root.leftChild = deleteRec(root.leftChild,index)
    elif root.data < index:
        root.rightChild = deleteRec(root.rightChild,index)
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
            min = findMinOfSubTree(root.rightChild)
            min.parent = root.parent
            root = min
            root.rightChild = deleteRec(root.rightChild,min.data)
    return root

def findPrevRec(node):
    if node == None:
        return node
    root = findRoot(node)
    if root == None:
        return root
    lst = []
    inOrderRec(root,lst)
    try:
        index = lst.index(root)
    except ValueError:
        print("The node is not in the BST")
        return None
    else:
        if index-1 > 0:
            return lst[index-1]
        else:
            return None

def findNextRec(node):
    if node == None:
        return node
    root = findRoot(node)
    if root == None:
        return root
    lst = []
    inOrderRec(root,lst)
    try:
        index = lst.index(root)
    except ValueError:
        print("The node is not in the BST")
        return None
    else:
        if index+1 < len(lst):
            return lst[index+1]
        else:
            return None


def findMinRec(node):
    if node == None:
        return node
    root = findRoot(node)
    lst = []
    inOrderRec(root,lst)
    return lst[0]


def findMaxRec(node):
    if node == None:
        return node
    root = findRoot(node)
    lst = []
    inOrderRec(root,lst)
    return lst[len(lst)-1]

#Recursive Helper Methods
def inOrderRec(root,empty_list):
    if root == None:
        return empty_list
    inOrderRec(root.leftChild,empty_list)
    empty_list.append(root)
    inOrderRec(root.rightChild,empty_list)
    return empty_list

def findRoot(root):
    if root == None:
        return None
    realroot = root
    while realroot.parent != None:
        realroot = root.parent
    return realroot

def findMinOfSubTree(node):
    if node == None:
        return node
    lst = []
    inOrderRec(root,lst)
    return lst[0]



#Iterative Functions

def insertIter(root,data,parent=None):
    if root == None:
        root = Node(data,parent)
        return
    current = root
    while current != None:
        if current.data > data:
            if current.leftChild == None:
                current.leftChild = Node(data,current)
                break
            current = current.leftChild
        else:
            if current.rightChild == None:
                current.rightChild = Node(data,current)
                break
            current = current.rightChild
    return

def deleteIter(root,index):
    isNone = False
    if root == None:
        return root
    current = root
    path = []
    while current != None:
        if current.data > index:
            path.insert(0,current)
            current = current.leftChild
        elif current.data < index:
            path.insert(0,current)
            current = current.rightChild
        else:
            if current.data != index:
                print("Node is not in Binary Search Tree")
                return
            break
    while current != None:
        if current.leftChild == None and current.rightChild == None:
            path.insert(0,current)
            current = None
            isNone = True
        elif current.leftChild == None:
            current.rightChild.parent = current.parent
            current = current.rightChild
            break
        elif current.rightChild == None:
            current.leftChild.parent = current.parent
            current = current.leftChild
            break
        else:
            lst = inOrderIter(root)
            i = lst.index(current)
            min = lst[i+1]
            min.parent = current.parent
            temp = current
            temp = min
            current = min.rightChild
            path.insert(0,current)
    while len(path) > 0:
        if isNone == False:
            temp = current
            pathNode = path.pop(0)
            if pathNode.data > temp.data:
                pathNode.leftChild = temp
            elif pathNode.data < temp.data:
                pathNode.rightChild = temp
            current = pathNode
            temp = current
        else:
            leaf = path.pop(0)
            pathNode = path.pop(0)
            if pathNode.data > leaf.data:
                pathNode.leftChild = None
            elif pathNode.data < leaf.data:
                pathNode.rightChild = None
            current = pathNode
            isNone = False


def findNextIter(root):
    if root == None:
        return root
    lst = inOrderIter(root)
    try:
        index = lst.index(root)
    except ValueError:
        print("The node is not in the BST")
        return None
    else:
        if index+1 < len(lst):
            return lst[index+1]
        else:
            return None

def findPrevIter(root):
    if root == None:
        return root
    lst = inOrderIter(root)
    try:
        index = lst.index(root)
    except ValueError:
        print("The node is not in the BST")
        return None
    else:
        if index-1 > 0:
            return lst[index-1]
        else:
            return None

def findMinIter(root):
    if root == None:
        return root
    lst = inOrderIter(root)
    return lst[0]

def findMaxIter(root):
    if root == None:
        return root
    lst = inOrderIter(root)
    return lst[len(lst)-1]

#Helper method
def inOrderIter(root):
    result_lst = []
    if root == None:
        return result_lst
    realroot = root
    while realroot.parent != None:
        realroot = realroot.parent
    stack = []
    current = realroot
    stack.insert(0,current)
    current = current.leftChild
    while len(stack) > 0 or current != None:
        if current != None:
            stack.insert(0,current)
            current = current.leftChild
        else:
            popped = stack.pop(0)
            result_lst.append(popped)
            current = popped.rightChild
    if current != None:
        result_lst.append(current)
    return result_lst

#Test Cases
root = Node(25)
insertRec(root,27,root)
insertRec(root,15,root)
insertRec(root,5,root)
insertRec(root,43,root)
insertRec(root,3,root)
for i in inOrderIter(root):
    print(i.data)
deleteIter(root,3)
insertIter(root,100,root)
insertIter(root,1,root)
print("\n")
for i in inOrderIter(root):
    print(i.data)
#print(root.leftChild.data)
#print(root.rightChild.data)
lst = []
print(inOrderIter(root))
print(inOrderRec(root,lst))
print(findPrevRec(root).data)
