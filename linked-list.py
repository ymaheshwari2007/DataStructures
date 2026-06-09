class Node:
  def __init__(self,val):
    self.val = val
    self.next = None
    self.prev = None


class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
  
  def append(self,val):
    newNode = Node(val)
    if self.head is None:
      self.head = newNode
      self.tail = newNode
    else:
      # traverssal = self.head
      # while traverssal.next is not None:
      #   traverssal = traverssal.next
      
      # newNode.prev = traverssal
      # traverssal.next = newNode
      # self.tail = newNode
      self.tail.next = newNode
      newNode.prev = self.tail
      self.tail = newNode
  
  def prepend(self,val):
    newNode = Node(val)
    if self.head is None:
      self.head = newNode
      self.tail = newNode
    else:
      newNode.next = self.head
      self.head.prev = newNode
      self.head = newNode
  
  def getLeft(self):
    firstNode = self.head
    self.head = firstNode.next
    return firstNode
  
  def getRight(self):
    lastNode = self.tail
    self.tail = lastNode.prev
    return lastNode

  