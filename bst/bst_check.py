INT_MAX = 4294967296
INT_MIN = -4294967296

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def checkBST(node, mini = INT_MIN, maxi = INT_MAX):
    if node == None:
        return True
    if node.data < mini or node.data > maxi:
        return False
    return checkBST(node.left, mini, node.data-1) and checkBST(node.right, node.data+1, maxi)

#        5
#    /      \
#   2        8
#  /  \     /  \
# 1    3   6    9

node1 = Node(1)
node3 = Node(3)
node2 = Node(2)
node2.left = node1
node2.right = node3

node6 = Node(6)
node9 = Node(9)
node8 = Node(8)
node8.left = node6
node8.right = node9

rootNode = Node(5)
rootNode.left = node2
rootNode.right = node8

print(checkBST(rootNode))