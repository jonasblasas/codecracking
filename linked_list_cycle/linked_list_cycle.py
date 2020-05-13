class LinkedListNode:
    def __init__(self, val):
        self.data = val
        self.next = None

def add_to_linked_list(head, node):
    cur = head
    while cur.next != None:
        cur = cur.next
    cur.next = node

def contains_cycle(head):
    slow = head.next
    fast = head.next.next
    maxi = 0
    while slow != None and fast != None and slow != fast and maxi < 1000:
        slow = slow.next
        if fast.next == None:
            return False
        fast = fast.next.next
        maxi += 1
    if slow is fast:
        return True
    return False

def print_linked_list(head):
    cur = head
    maxi = 0
    while cur != None and maxi < 1000:
        print(cur.data)
        cur = cur.next
        maxi += 1

cycle_head = LinkedListNode(1)
add_to_linked_list(cycle_head, LinkedListNode(2))
add_to_linked_list(cycle_head, LinkedListNode(3))
add_to_linked_list(cycle_head, LinkedListNode(4))
add_to_linked_list(cycle_head, LinkedListNode(5))
add_to_linked_list(cycle_head, LinkedListNode(6))
cycle_node = LinkedListNode(7)
cycle_node.next = cycle_head
add_to_linked_list(cycle_head, cycle_node)

print(contains_cycle(cycle_head))
print_linked_list(cycle_head)

non_cycle_head = LinkedListNode(1)
add_to_linked_list(non_cycle_head, LinkedListNode(2))
add_to_linked_list(non_cycle_head, LinkedListNode(3))
add_to_linked_list(non_cycle_head, LinkedListNode(4))
add_to_linked_list(non_cycle_head, LinkedListNode(5))
add_to_linked_list(non_cycle_head, LinkedListNode(6))
add_to_linked_list(non_cycle_head, LinkedListNode(7))

print(contains_cycle(non_cycle_head))
print_linked_list(non_cycle_head)