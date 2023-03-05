'''
110. Balanced Binary Tree

Given a binary tree, determine if it is 
height-balanced. 

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: true

Example 2
Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
'''

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

def isBalanced(root):

    def height(root):
        if root is None:
            return 0
        return 1 + max(height(root.left), height(root.right))
    
    if not root:
        return True
    
    left_height = height(root.left)
    right_height = height(root.right)
    
    if abs(left_height - right_height) > 1:
        return False
    
    return isBalanced(root.left) and isBalanced(root.right)


a = TreeNode(3)
b = TreeNode(9)
c = TreeNode(20)
d = TreeNode(15)
e = TreeNode(7)
f = None
g = None
a.left = b
a.right = c
b.left = f
b.right = g
c.left = d 
c.right = e

#     1
#    / \
#   2   3
#      /  \
#     4    5

aa = TreeNode(1)
bb = TreeNode(2)
cc = TreeNode(2)
dd = TreeNode(3)
ee = TreeNode(3)
ff = TreeNode(4)
gg = TreeNode(4)
hh = None
aa.left = bb
aa.right = cc
cc.left = dd
cc.right = ee
dd.left = ff
dd.right = gg

#             1
#           /   \
#          2     2
#        /   \
#       3     3
#     /  \
#    4    4 




if __name__ == "__main__":

    true_tree = bfs(a)
    print(true_tree) # [3, 9, 20, None, None, 15, 7]
    
    false_tree = bfs(aa)
    print(false_tree) # [1, 2, 2, 3, 3, None, None, 4, 4]

    t1 = isBalanced(a)
    print(t1) # true

    t2 = isBalanced(aa)
    print(t2) # False