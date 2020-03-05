import ArraysOfIntegers as part3
import IterativeBST
import AVLTree

randomlst = part3.getRandomArray(10000)
randomavlroot = AVLTree.Node(randomlst[0],None)
randombstroot = IterativeBST.Node(randomlst[0],None)
randomAVLtree = AVLTree.AVLTree(randomavlroot)
randomBST = IterativeBST.IterBST(randombstroot)
sortedlst = part3.getSortedArray(10000)
sortedavlroot = AVLTree.Node(sortedlst[0],None)
sortedbstroot = IterativeBST.Node(sortedlst[0],None)
sortedAVLtree = AVLTree.AVLTree(sortedavlroot)
sortedBST = IterativeBST.IterBST(sortedbstroot)
for i in range(1,10000):
    randomAVLtree.insertIter(randomlst[i])
    randomBST.insertIter(randomlst[i])
    sortedAVLtree.insertIter(sortedlst[i])
    sortedBST.insertIter(sortedlst[i])

print("Number of Traversals in AVL Tree with getRandomArray: ",randomAVLtree.traversalCounter)
print("Number of Traversals in BST with getRandomArray: ",randomBST.traversalCounter)
print("Number of Traversals in AVL Tree with getSortedArray: ",sortedAVLtree.traversalCounter)
print("Number of Traversals in BST with getSortedArray: ",sortedBST.traversalCounter)
