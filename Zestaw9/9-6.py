from tree_node import Node

def count_leafs(node):
    if node is None:
        return 0
    if(node.left is None and node.right is None):
        return 1
    else:
        return count_leafs(node.left) + count_leafs(node.right)

def count_total(node):
    if node is None:
        return 0

    if(node.left is None and node.right is None):
        return node.data
    
    if node.left is not None and node.right is not None:
        return node.data + count_total(node.left) + count_total(node.right)

    if node.left is not None:
        return node.data + count_total(node.left)
    
    if node.right is not None:
        return node.data + count_total(node.right)


if __name__ == "__main__":
    top = Node(1)
    top.left = Node(2)
    top.right = Node(3)
    top.left.left = Node(5)
    top.left.right = Node(5)
    top.right.left = Node(6)
    top.right.right = Node(7)

    print(count_leafs(top))
    print(count_total(top))
