class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def make_list(v):
    if not v: return None
    node = ListNode(v[0])
    node.next = make_list(v[1:])
    return node

def print_list(head):
    while head:
        print(head.val, '', end='')
        head = head.next
    print()