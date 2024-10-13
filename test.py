class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def tree_insert(root, value):
    if not root:
        return TreeNode(value)
    if value <= root.value:
        root.left = tree_insert(root.left, value)
    else:
        root.right = tree_insert(root.right, value)
    return root

def visualize_tree(root, indent="", level=0):
    if not root:
        return
    visualize_tree(root.right, indent + "    ", level + 1)
    print(indent + str(root.value))
    visualize_tree(root.left, indent + "    ", level + 1)

# Sample Input (15 elements)
input_values = [15, 6, 18, 3, 7, 17, 20, 2, 4, 13, 9, 1, 5, 12, 10]

tree_root = None
for val in input_values:
    tree_root = tree_insert(tree_root, val)

print("\nBinary Search Tree Visualization:")
visualize_tree(tree_root)