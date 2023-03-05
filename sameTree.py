'''
100. Same Tree

Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

Example 1:
Input: p = [1,2,3], q = [1,2,3]
Output: true

Example 2:
Input: p = [1,2], q = [1,null,2]
Output: false

Example 3:
Input: p = [1,2,1], q = [1,1,2]
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
        if current is None:
            values.append(None)
            continue
        values.append(current.val)
        queue.append(current.left if current.left else None)
        queue.append(current.right if current.right else None)
    # Remove trailing None values
    while values and values[-1] is None:
        values.pop()
    return values

def isSame(p, q):
    a = bfs(p)
    b = bfs(q)

    return a == b




        



a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
a.left = b
a.right = c
a1 = TreeNode(1)
b1 = TreeNode(2)
c1 = TreeNode(3)
a1.left = b1
a1.right = c1
#     1                 1     
#    / \    and        / \
#   2   3             2   3
aa = TreeNode(1)
bb = TreeNode(2)
aa.left = bb
aa1 = TreeNode(1)
bb1 = TreeNode(2)
aa1.right = bb1
#     1            1     
#    /     and      \
#   2                2
aaa = TreeNode(1)
bbb = TreeNode(1)
ccc = TreeNode(2)
aaa.left = ccc
aaa.right = bbb
aaa1 = TreeNode(1)
bbb1 = TreeNode(1)
ccc1 = TreeNode(2)
aaa1.left = bbb1
aaa1.right = ccc1

#     1                 1     
#    / \    and        / \
#   2   1             1   2

if __name__ == "__main__":
    t1 = bfs(a)
    print(t1)
    t1o = bfs(a1)
    print(t1o)
    print(isSame(a,a1)) # True

    t2 = bfs(aa)
    print('\n',t2)
    t2o = bfs(aa1)
    print(t2o)
    print(isSame(aa,aa1)) # False

    t3 = bfs(aaa)
    print('\n',t3)
    t3o = bfs(aaa1)
    print(t3o)
    print(isSame(aaa,aaa1)) # False
