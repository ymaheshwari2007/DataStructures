# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #Finding the length of the linked list
        counter = 1
        node = head
        while True:
            node = node.next
            if node is not None:
                counter +=1
            else:
                break
        
        traversal = counter//2
        node = head
        for i in range(traversal):
            node = node.next
        return node
      
      
  '''Optimal solution'''
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        f=head
        s=head
        while f and f.next:
            f=f.next.next
            s=s.next
        return s