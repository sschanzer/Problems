class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right 

def bfs(root):
    if root is None:
        return None
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

def maxDepth(root):
    
    counter = 0
    if root is None:
        return 0
    else:
        counter += 1
    max_depth = counter + max(maxDepth(root.left), maxDepth(root.right))

    return max_depth


a = TreeNode(3)
b = TreeNode(9)
c = TreeNode(20)
d = TreeNode(15)
e = TreeNode(7)
a.left = b
a.right = c
c.left = d
c.right = e
#    3
#   / \
#  9   20
#     /  \
#    15   7

if __name__ == "__main__":
    my_tree = bfs(a)
    print(my_tree)

    depth1 = maxDepth(a)
    print(depth1) # 3

    