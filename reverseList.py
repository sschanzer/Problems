class LinkNode:
    def __init__(self, val=0, next = None):
        self.val = val
        self.next = next

def reverseList(head: LinkNode):
    # Initialize three pointers
    prev = None
    current = head
    next_node = None

    while current:
        # store the next node
        next_node = current.next

        # reverse the current nodes pointer to point to the previous node
        current.next = prev

        # update the previous and current nodes for the next iteration
        prev = current
        current = next_node

    # set the new head of the reversed linked list to be the last node (previously the tail)
    head = prev

    # return the new head
    return head

# create linked list 
node5 = LinkNode(5, None)
node4 = LinkNode(4, node5)
node3 = LinkNode(3, node4)
node2 = LinkNode(2, node3)
node1 = LinkNode(1, node2)
head = node1

# print above linked list
current = head
while current:
    print(current.val, end="->")
    current = current.next

# reverse the above linked list
head = reverseList(head)

# print the reverse list
current = head
print('\n Reversed linked list: ')
while current:
    print(current.val, end='->')
    current = current.next
