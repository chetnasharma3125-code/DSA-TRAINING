class GetNode:
    def __init__(self):
        self.Data=None
        self.next=None
    
    
class LinkedList:
    def __init__(self):
        self.head=None   
    
    def append(self):
        Data=int(input("Enter data :"))
        newNode=GetNode()
        newNode.Data=Data
        if self.head==None:
            self.head=newNode
        else:
            ptr=self.head
            while ptr.next!=None:
                ptr=ptr.next
            ptr.next=newNode
            print(Data, "is added")        
       
    
    def traverse(self): 
        if self.head==None:
            print("Linked list not present")
        else:
            ptr=self.head
            while ptr!=None:
                print(ptr.Data," -> ", end=" ")     
                ptr=ptr.next
                
    def AddatBegin(self):
        Data=int(input("Enter data :"))
        key=int(input("Enter data after inserted: "))
        newNode=GetNode()
        newNode.Data=Data
        if self.head==None:
            self.head=newNode
        else:
            ptr=self.head
            newNode.next=ptr
            self.head=newNode
            print(" Node is added at Begin")
         
    def AddinBetween(self):
         Data=int(input("Enter data :"))
         key=int(input("Enter data after inserted: "))
         newNode=GetNode()
         newNode.Data=Data
         if self.head==None:
            self.head=newNode
         else:
             ptr=self.head
             while  ptr.next!= None :
                 if key == ptr.Data:
                    break;
                 else:
                     ptr = ptr.next
                 if ptr.next==None:
                     print("key not found ")  
                 else:
                           
                  ptr1=ptr.next
                  ptr.next=newNode
                  newNode.next=ptr1
                  print( Data, "Data is added in between")
                  
                  
    def DeleteatBegin(self):
        if self.head==None:
            print("List not present")
        else:
            ptr=self.head
            ptr1=ptr.next
            ptr.next=None
            head=ptr1
            print(ptr.Data, " Is deleted:" )                  
                     
                
            
    
if __name__ =='__main__' :
     obj=LinkedList()
     while True:
         print("1. Append ")  
         print("2. Traverse ") 
         print("3. Add at Begin")
         print("4. Add in Between")
         print("5. Delete at Begin")
         print("0. exit")  
         n = int(input("select any choice:"))
         if n == 1:
             obj.append()
         elif n == 2:
             obj.traverse()
         elif n == 3:
             obj.AddatBegin() 
         elif n == 4:
             obj.AddinBetween()  
         elif n == 5:
             obj.DeleteatBegin()      
         elif n == 0:
             obj.exit(0)