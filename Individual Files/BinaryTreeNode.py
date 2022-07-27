class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None


def sort_binary_tree(nodes):
    unsorted = True
    while unsorted:
        for i in range(len(nodes)-1):
            if nodes[i].data >= nodes[i+1].data:
                continue
                print("continuing")
            else:
                print("breaking")
                break
            unsorted = False
        # print("check")


node1 = BinaryTreeNode(50)
node2 = BinaryTreeNode(27)
node3 = BinaryTreeNode(75)
node4 = BinaryTreeNode(11)
node5 = BinaryTreeNode(35)
node6 = BinaryTreeNode(30)
node7 = BinaryTreeNode(88)

"""
node1.leftChild = node2
node1.rightChild = node3
node2.leftChild = node4
node2.rightChild = node5
node3.leftChild = node6
node3.rightChild = node7
"""

nodes = [node1, node2, node3, node4, node5, node6, node7]

nodes[0].leftChild = nodes[1]
nodes[0].rightChild = nodes[2]
nodes[1].leftChild = nodes[3]
nodes[1].rightChild = nodes[4]
nodes[2].leftChild = nodes[5]
nodes[2].rightChild = nodes[6]

temp = nodes[0]
tempinx = 0

print("Root Node is:")
print(node1.data)

print("left child of the node is:")
print(node1.leftChild.data)

print("right child of the node is:")
print(node1.rightChild.data)

print("Node is:")
print(node2.data)

print("left child of the node is:")
print(node2.leftChild.data)

print("right child of the node is:")
print(node2.rightChild.data)

print("Node is:")
print(node3.data)

print("left child of the node is:")
print(node3.leftChild.data)

print("right child of the node is:")
print(node3.rightChild.data)

print("Node is:")
print(node4.data)

print("left child of the node is:")
print(node4.leftChild)

print("right child of the node is:")
print(node4.rightChild)

print("Node is:")
print(node5.data)

print("left child of the node is:")
print(node5.leftChild)

print("right child of the node is:")
print(node5.rightChild)

print("Node is:")
print(node6.data)

print("left child of the node is:")
print(node6.leftChild)

print("right child of the node is:")
print(node6.rightChild)

print("Node is:")
print(node7.data)

print("left child of the node is:")
print(node7.leftChild)

print("right child of the node is:")
print(node7.rightChild)

sort_binary_tree(nodes)



