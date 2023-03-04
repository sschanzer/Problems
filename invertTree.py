class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


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

def invertTree(root):
    if root is None:
        return None
    
    values = []
    queue  = [root]
    while len(queue) > 0:
        current = queue.pop(0)
        values.append(current.val)
        temp = current.left
        if current.left:
            current.left = current.right
            queue.append(current.left)
        if current.right:
            current.right = temp
            queue.append(current.right)

    return values

a = TreeNode(4)
b = TreeNode(2)
c = TreeNode(7)
d = TreeNode(1)
e = TreeNode(3)
f = TreeNode(6)
g = TreeNode(9)
a.left = b
a.right = c
b.right = e
b.left = d
c.right = g
c.left = f
#        4
#     /     \
#    2       7
#  /  \    /   \
# 1    3  6     9



if __name__ == "__main__":

    my_tree = bfs(a)
    print(my_tree)

    invert = invertTree(a)
    print(invert)


# The above solution only runs locally. The following solution was accepted by LeetCode:

# def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    
    # if root is None:
    #     return None

    # temp = root.left
    # root.left = root.right
    # root.right = temp

    # self.invertTree(root.left)
    # self.invertTree(root.right)

    # return root