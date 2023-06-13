class Node:
  def __init__(self, e, n):
    self.element = e
    self.next = n

class SinglyList:  
  def __init__(self, a): #  Creates a non dummy headed non circular linked list using the values from the given array.
    self.head = Node(a[0],None)
    tail = self.head
    i = 1
    while i < len(a):
      n = Node(a[i],None)
      tail.next = n
      tail = n
      i += 1

  def forwardprint(self): # prints the elements in the list
    tail = self.head
    s = " "
    while tail != None:
      s+= str(tail.element)+ " "
      tail = tail.next
    print(s)
      

  def merge(self, a, b): # Merges two linked lists a and b with only non duplicate elements and returns the merged linked list's head reference
    arr = []
    tail = a.head
    while tail.next != None:
      if tail.element not in arr:
        arr += [tail.element]
      tail = tail.next
    
    tail = b.head
    while tail != None:
      if tail.element not in arr:
        arr += [tail.element]
      tail = tail.next
    return SinglyList(arr)




a1 = [1,2,1,4,5,7]
a2=[9,4,6]
l1 = SinglyList(a1)
l1.forwardprint() # this should print: 1, 2, 1, 4, 5, 7.
l2 = SinglyList(a2)
l2.forwardprint() # this should print: 9, 4, 6.
m = l1.merge(l1,l2) 
m.forwardprint() # this should print: 1, 2, 4, 5, 7, 9, 6.