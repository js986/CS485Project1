class Node:
    def __init__(self,data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

def sort(array):
    result_lst = []
    if len(array) == 0:
        return result_lst
    root = Node(array[0])
    for i in range(1,len(array)):
        insert(root,array[i])
    inOrder(root,result_lst)
    return result_lst

#Helper Functions
def insert(root,data):
    if root == None:
        root = Node(data)
        return root
    elif root.data > data:
        root.leftChild = insert(root.leftChild,data)
    else:
        root.rightChild = insert(root.rightChild,data)
    return root
def inOrder(root,empty_list):
    if root == None:
        return empty_list
    inOrder(root.leftChild,empty_list)
    empty_list.append(root.data)
    inOrder(root.rightChild,empty_list)
    return empty_list

#Test Case
arr = [10,8,15,9,13,20]
print(sort(arr))
