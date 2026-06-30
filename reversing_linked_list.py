# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head):
      if not head:
        return None
      prev = None
      current = head
      while current:
        after = current.next
        current.next = prev
        prev = current
        current = after
      return prev