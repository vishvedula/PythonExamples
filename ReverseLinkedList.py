'''
Reversing a LinkedList in Python
'''

def reverse(head):
  prev, current = None, head
  while current is not None:
    tmp = current.next
    current.next = prev
    prev = current
    current = tmp
return prev
