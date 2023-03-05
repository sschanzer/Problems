'''
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.
'''

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def dfs(root):
    if root is None:
        return []
    values = []
    stack = [root]
    while len(stack) > 0:
        current = stack.pop()
        values.append(current.val)
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)
    return values

def bfs(root):
    if root is None:
        return []
    
    values = []
    queue = [root]
    while len(queue) > 0:
        current = queue.pop(0)
        values.append(current.val)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    
    return values


def diameterOfBinaryTree(root):

    def height(root):
        if root is None:
            return 0

        return 1 + max(height(root.left), height(root.right))
    
    if root is None:
        return 0
    lheight = height(root.left)
    rheight = height(root.right)
    
    ldiameter = diameterOfBinaryTree(root.left)
    rdiameter = diameterOfBinaryTree(root.right)

    return max(lheight + rheight, max(ldiameter, rdiameter))

def alt_diameter(root):
    if root is None:
        return 0
    
    max_diameter = 0
    stack = [(root, False)]
    heights = {None: 0}

    while stack:
        node, visited = stack.pop()
    
        if visited:
            lheight = heights[node.left]
            rheight = heights[node.right]
            diameter = lheight + rheight 
            max_diameter = max(max_diameter, diameter)
            heights[node] = 1 + max(lheight, rheight)
        else:
            stack.append((node, True))
            if node.right:
                stack.append((node.right, False))
            if node.left:
                stack.append((node.left, False))

    return max_diameter



            
a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)

a.left = b
a.right = c
b.left = d
b.right = e


#       1
#     /   \
#    2      3
#   / \
#  4   5



if __name__ == "__main__":
    my_tree = dfs(a)
    print('dfs: ',my_tree)
    el_tree = bfs(a)
    print('bfs: ', el_tree)

    # my_depth = height(a)
    # print(my_depth) # 6

    my_diameter = diameterOfBinaryTree(a)
    print(my_diameter) # GOAL = 3

    alt_diam = alt_diameter(a)
    print(alt_diam) # GOAL = 3

   