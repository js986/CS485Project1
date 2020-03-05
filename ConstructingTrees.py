from ArraysOfIntegers import *
import AVLTree
import RecursiveBST

lst = getRandomArray(10000)
recroot = RecursiveBST.Node(lst[0],None)
avlroot = AVLTree.Node(lst[0],None)
RecTree = RecursiveBST.RecBST(recroot)
AVLtree = AVLTree.AVLTree(avlroot)
for i in range(1,len(lst)):
    RecTree.insertRec(RecTree.root,lst[i])
    AVLtree.insertIter(lst[i])

#RecTree.printTree(RecTree.root)
