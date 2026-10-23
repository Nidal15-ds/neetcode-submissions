class Node:
    def __init__(self ,val:int):
        self.val = val 
        self.next = None

class LinkedList:
    
    def __init__(self):
      self.head =None

         
    
    def get(self, index: int) -> int:
        current = self.head
        count = 0
        while current:
            if count == index:
                 return current.val
            current = current.next
            count = count + 1

        return -1

        

    def insertHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def insertTail(self, val: int) -> None:
        new_node = Node(val)

        if self.head is None:
           self.head = new_node
           return
        current_node = self.head
        while current_node.next is not None:
            # increment until we find last node
            current_node =  current_node.next

        current_node.next = new_node    

    def remove(self, index: int) -> bool:
         # case 1 : empty list
        if index < 0 or self.head == None :
           return False 
        
        #case 2 : one node in list (head)
        if index == 0:
            self.head = self.head.next
            return True 
        # case 3 : in the middale 
        current = self.head 

        for i in range(index -1):
            if current.next == None :
               return False 
            current = current.next
        
        if current.next == None :
           return False
        

        current.next = current.next.next
        return True

    def getValues(self) -> List[int]:
        arr = []
        current = self.head
        while current:
            arr.append(current.val)
            current = current.next 
        return arr    
        
